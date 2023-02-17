from rest_framework import serializers
from movies.models import Movies, Actors, Movies_Actors

class MoviesSerializer(serializers.ModelSerializer):
    actors_count = serializers.IntegerField()
    class Meta:
        model = Movies
        fields = ('MovieID', 'Title', 'Description', 'release_date', 'actors_count','likes')



class ActorsSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField()
    
    class Meta:
        model = Actors
        fields = ("ActorID","Name","DOB","movies_count")
