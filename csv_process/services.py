import logging
from io import StringIO

import pandas as pd
import requests

from django.db import transaction

from city.models import City
from csv_process.models import CSVFile, CSVFileDataType, CSVFileUploadStatus
from csv_process.tasks import process_csv_file


logger = logging.getLogger(__name__)


def upload_csv_file(link: str) -> CSVFile:
    file = CSVFile.objects.create(link=link)

    process_csv_file.delay(file.id)

    return file


CSV_CHUNK_SIZE = 1000


class CSVFileUploadService:
    def __init__(self, file_id: int):
        self.file_id = file_id
        self.file = CSVFile.objects.get(id=file_id)

    @transaction.atomic
    def upload(self):
        """
        Downloads a CSV file from a provided link, processes it in chunks,
        parses date fields, and stores each row of data.
        Updates the upload status of the associated file upon completion or failure.
        """
        try:
            with requests.get(self.file.link, stream=True) as response:
                response.raise_for_status()

                csv_buffer = StringIO()

                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    csv_buffer.write(chunk.decode("utf-8"))
                    csv_buffer.seek(0)

                    for data_chunk in pd.read_csv(
                        csv_buffer,
                        chunksize=CSV_CHUNK_SIZE,
                        parse_dates=self._get_date_fields(),
                        infer_datetime_format=True,
                    ):
                        for _, row in data_chunk.iterrows():
                            self.store_data(row)

                    csv_buffer.seek(0)
                csv_buffer.truncate(0)

                self.file.update_upload_status(CSVFileUploadStatus.FINISHED)

        except Exception as error:
            logger.error(error)

            self.file.update_upload_status(CSVFileUploadStatus.FAILED)

    def store_data(self, data: dict) -> None:
        if self.file.data_type == CSVFileDataType.CITIES:
            City.objects.create(
                csv_file=self.file,
                name=data["name"],
                description=data["description"],
                population=data["population"],
                established_at=data["established_at"],
            )

    def _get_date_fields(self) -> list[str]:
        if self.file.data_type == CSVFileDataType.CITIES:
            return ["established_at"]

        return []
