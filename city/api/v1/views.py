from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from city.api.v1.filters import CityFilter
from city.api.v1.serializers import CitySerializer
from city.selectors import CitySelector


class CityListAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    selector = CitySelector
    filterset_class = CityFilter

    @swagger_auto_schema(tags=["city"], operation_id="Cities")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.selector.get_cities()
