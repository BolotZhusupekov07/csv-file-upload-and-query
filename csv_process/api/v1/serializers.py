from rest_framework import serializers

from csv_process.models import CSVFile, CSVFileDataType


class CSVUploadInputSerializer(serializers.Serializer):
    link = serializers.URLField()
    data_type = serializers.ChoiceField(choices=CSVFileDataType.choices)


class CSVUploadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = ["id", "link", "upload_status", "created_at"]
