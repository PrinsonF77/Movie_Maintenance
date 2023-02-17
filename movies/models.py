from django.db import models

# Create your models here.
class Movies(models.Model):
    MovieID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    release_date = models.DateField()
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.Title

class Actors(models.Model):
    ActorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    DOB = models.DateField()

    def __str__(self) -> str:
        return self.Name

class Movies_Actors(models.Model):
    Movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    Actor = models.ForeignKey(Actors, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("Movie","Actor")

    def __str__(self) -> str:
        return self.Movie.Title + "_" + self.Actor.Name