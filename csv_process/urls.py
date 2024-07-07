from django.urls import include, path

urlpatterns = [path("api/v1/", include("csv_process.api.v1.urls"))]
