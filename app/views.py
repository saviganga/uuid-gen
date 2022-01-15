from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.models import UUIDModel
from .serializers import UUIDModelSerializer
import uuid

class UUIDgenApiView(APIView):

    def get(self, request, *args, **kwargs):

        UUIDModel.objects.create(uid=uuid.uuid4())
        uids = UUIDModel.objects.all()
        serializer = UUIDModelSerializer(uids, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

