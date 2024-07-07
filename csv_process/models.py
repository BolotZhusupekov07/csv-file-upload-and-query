from django.db import models
from django.utils import timezone


class CSVFileUploadStatus(models.TextChoices):
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class CSVFileDataType(models.TextChoices):
    CITIES = "CITIES"


class CSVFile(models.Model):
    link = models.URLField()
    data_type = models.CharField(
        max_length=20,
        choices=CSVFileDataType.choices,
        default=CSVFileDataType.CITIES,
    )
    upload_status = models.CharField(
        max_length=20,
        choices=CSVFileUploadStatus.choices,
        default=CSVFileUploadStatus.IN_PROGRESS,
    )
    created_at = models.DateTimeField(db_index=True, default=timezone.now)

    def update_upload_status(self, status: CSVFileUploadStatus):
        self.upload_status = status
        self.save(update_fields=("upload_status",))
