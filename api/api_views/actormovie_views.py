from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import actormovieModel
from ..serializers import actormovieSerializer

class actormovieView(APIView):

    def get(self, request):
        actormovie = actormovieModel.objects.all()
        serializer = actormovieSerializer(actormovie, many=True)
        return Response({"res": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = actormovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"res": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR_in_query": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class actormovieSingleView(APIView):

    def get_actormovie(self, pk):
        try:
            return actormovieModel.objects.get(pk=pk)
        except actormovieModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
            actormovie = self.get_actormovie(pk)
            serializer = actormovieSerializer(actormovie)
            return Response(serializer.data)

    def put(self, request, pk):
        actormovie = self.get_actormovie(pk=pk)
        serializer = actormovieSerializer(
            actormovie,
            data=request.data
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response({"res": serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"ERROR_in_query":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        actormovie = self.get_actormovie(pk=pk)
        serializer = actormovieSerializer(
            actormovie,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({"res": serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"ERROR_in_query": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        actormovie = self.get_actormovie(pk=pk)
        actormovie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)