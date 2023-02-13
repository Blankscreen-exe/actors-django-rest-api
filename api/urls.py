from django.urls import path
from .api_views.actor_views import *
from .api_views.movie_views import *
from .api_views.actormovie_views import *
from .api_views.fileview import *

urlpatterns = [
    # url for actors
    path('actors/', actorView.as_view(), name='actors'),
    path('actors/<int:pk>/', actorSingleView.as_view(), name='actorOne'),
    # url for movies
    path('movies/', movieView.as_view(), name='movies'),
    path('movies/<int:pk>/', movieSingleView.as_view(), name='movieOne'),
    # url for actors and movie relations
    path('actormovie/', actormovieView.as_view(), name='actormovie'),
    path('actormovie/<int:pk>/', actormovieSingleView.as_view(), name='actormovieOne'),
    # url for file upload
    path('file/actors/', actorFileView.as_view(), name='csv_upload')
    # path('file/movies/', movieFileView.as_view(), name='csv_upload')
    # path('file/actormovies/', actormovieFileView.as_view(), name='csv_upload')
]
