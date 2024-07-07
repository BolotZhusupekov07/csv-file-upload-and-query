from rest_framework import serializers

from city.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "description", "population", "established_at", "csv_file_id"]
