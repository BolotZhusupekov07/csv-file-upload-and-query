from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.typing import HttpRequestWithData
from common.utils import (
    get_exception_response,
    get_response,
    is_serializer_valid,
)
from csv_process.api.v1.serializers import (
    CSVUploadInputSerializer,
    CSVUploadOutputSerializer,
)
from csv_process.services import upload_csv_file


class CSVUploadView(APIView):
    input_serializer_class = CSVUploadInputSerializer
    output_serializer_class = CSVUploadOutputSerializer

    @swagger_auto_schema(
        tags=["csv"],
        operation_id="CSV File Upload",
        request_body=input_serializer_class,
        responses={
            status.HTTP_200_OK: openapi.Response(
                "CSV File Upload Have Started Successfully",
                output_serializer_class,
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                "The request validation has failed"
            ),
        },
    )
    def post(self, request: HttpRequestWithData) -> Response:
        serializer = self.input_serializer_class(data=request.data)
        if error := is_serializer_valid(serializer):
            return error

        link = serializer.validated_data["link"]

        try:
            file = upload_csv_file(link)
            return get_response(
                self.output_serializer_class(file).data,
                status.HTTP_200_OK,
            )
        except Exception as error:
            return get_exception_response(error)
