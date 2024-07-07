from config.celery import app


@app.task(name="csv_process.upload")
def process_csv_file(file_id: int):
    from csv_process.services import CSVFileUploadService

    service = CSVFileUploadService(file_id)
    service.upload()
