from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import movieModel
from ..serializers import movieSerializer

class movieView(APIView):

    def get(self, request):
        movies = movieModel.objects.all()
        serializer = movieSerializer(movies, many=True)
        return Response({"res": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = movieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"res": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR_in_query": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class movieSingleView(APIView):

    def get_movie(self, pk):
        try:
            return movieModel.objects.get(pk=pk)
        except movieModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        movie = self.get_movie(pk)
        serializer = movieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = self.get_movie(pk)
        serializer = movieSerializer(
            movie,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({"res": serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"PK_not_found": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        movie = self.get_movie(pk)
        serializer = movieSerializer(
            movie,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            return Response({"res": serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"PK_not_found": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = self.get_movie(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)