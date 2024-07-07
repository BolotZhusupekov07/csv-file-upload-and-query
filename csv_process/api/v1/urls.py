from django.urls import path

from csv_process.api.v1 import views

urlpatterns = [
    path(
        "upload-csv/",
        views.CSVUploadView.as_view(),
        name="upload-csv",
    )
]
