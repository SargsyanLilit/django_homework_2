from django.urls import path
from tables import views

urlpatterns = [
    path('movies-rate-5/', views.movies_rate_five),
    path('add/', views.add_movie),
    path('delete/', views.delete_movie),
]
