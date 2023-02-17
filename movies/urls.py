from django.urls import path
from movies import views

urlpatterns = [
    path('movies/',views.moviesApi, name="movies"),
    path('actors/',views.actorsApi, name="actors"),
    path('movies/like/<int:id>', views.addLike, name="like"),
    path('movies/unlike/<int:id>',views.delLike, name="unlike")
]