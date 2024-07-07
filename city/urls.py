from django.urls import include, path

urlpatterns = [path("api/v1/", include("city.api.v1.urls"))]
