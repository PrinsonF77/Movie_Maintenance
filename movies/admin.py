from django.contrib import admin
from .models import Movies, Actors, Movies_Actors
# Register your models here.

admin.site.register(Movies)
admin.site.register(Actors)
admin.site.register(Movies_Actors)