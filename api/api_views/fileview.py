from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from ..models import FileModel
from ..serializers import FileSerializer

class actorFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    # def add_to_filemodel(self, serializer):
    #     file = self.request.data.get('file')

    def post(self, request):
        file = request.data.get('file')

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)