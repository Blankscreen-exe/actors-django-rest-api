from rest_framework import serializers
from .models import actorModel, actormovieModel, movieModel, File

class actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = actorModel
        fields = ('__all__')

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movieModel
        fields = ('__all__')

class actormovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = actormovieModel
        fields = ('__all__')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'