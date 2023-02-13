from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import actorModel
from ..serializers import actorSerializer


class actorView(APIView):

    def get(self, request):
        actors = actorModel.objects.all()
        serializer =  actorSerializer(actors, many=True)
        return Response({"res": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = actorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR_in_query": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class actorSingleView(APIView):

    def get_actor(self, pk):
        try:
            return actorModel.objects.get(pk=pk)
        except actorModel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        actor = self.get_actor(pk)
        serializer = actorSerializer(actor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        actor = self.get_actor(pk=pk)
        serializer = actorSerializer(
            actor,
            data=request.data
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response({"res":serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"PK_not_found": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        actor = self.get_actor(pk=pk)
        serializer = actorSerializer(
            actor,
            data=request.data,
            partial=True
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response({"res":serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"PK_not_found": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        actor = self.get_actor(pk=pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    