from django.contrib import admin
from .models import actorModel, movieModel, actormovieModel

# app_used: API
class actorAdmin(admin.ModelAdmin):
    list_display = ('id','name','oscar','height','dob',)

admin.site.register(actorModel, actorAdmin)

class movieAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','imdb_rating','release_date')

admin.site.register(movieModel, movieAdmin)

class actormovieAdmin(admin.ModelAdmin):
    list_display = ('id','actor','movie')

admin.site.register(actormovieModel, actormovieAdmin)

