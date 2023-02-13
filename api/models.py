from django.db import models
from django.utils.timezone import now

class actorModel(models.Model):
    """
    model for the actor table
    """
    name = models.CharField(max_length=100)
    oscar = models.BooleanField(default=False)
    height = models.FloatField()
    dob = models.DateField(default=now)
    
    def __str__(self):
        return self.name

class movieModel(models.Model):
    """
    model for the movie table
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    release_date = models.DateField(default=now)
    imdb_rating = models.FloatField(default=0)
    actors = models.ManyToManyField(actorModel, through='actormovieModel')
    
    def __str__(self):
        return self.name

class actormovieModel(models.Model):
    """
    model for the actormovie table which represents each relation between an actor and the movie they were cast in
    """
    actor = models.ForeignKey(actorModel, on_delete=models.CASCADE)
    movie = models.ForeignKey(movieModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Actor:{self.actor} Movie:{self.movie}'
    
class FileModel(models.Model):
    """
    model for the csv file inputs
    """
    file = models.FileField(upload_to='files/')