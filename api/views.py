from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import actorModel, movieModel, actormovieModel
from .serializers import actorSerializer, movieSerializer, actormovieSerializer

# !!! environment variables
import environ
env = environ.Env()
environ.Env.read_env()

import os
PRODUCTION = os.environ.get('PRODUCTION', default=False)


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

class actormovieView(APIView):

    def get(self, request):
        actormovie = actormovieModel.objects.all()
        serializer = actorSerializer(actormovie, many=True)
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
