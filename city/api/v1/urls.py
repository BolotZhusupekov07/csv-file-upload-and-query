from django.urls import path

from city.api.v1 import views

urlpatterns = [
    path(
        "cities/",
        views.CityListAPI.as_view(),
        name="cities",
    )
]
