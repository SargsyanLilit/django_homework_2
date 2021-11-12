from django.shortcuts import render, HttpResponse
from tables.models import Film
# Create your views here.


def movies_rate_five(request):
    filtered_movies = Film.objects.filter(rate=5)
    output = "The movies having rate of 5:\n"
    for i in filtered_movies:
        output += " " + str(i)
    return HttpResponse(output)


def add_movie(request):
    new_movie = Film(name=input("Enter the name:\n"),
                     rate=int(input("Enter the rate:\n")),
                     is_published=bool(input("Is the movie published? Enter True or False\n")),
                     status=int(input("If the movie is new enter 0, otherwise 1\n")))
    new_movie.save()
    return HttpResponse(f"New movie was added at {new_movie.created_at}: {str(new_movie)}")


def delete_movie(request):
    del_movie = input("Enter the name of the movie you want to delete\n")
    Film.objects.filter(name=del_movie).delete()
    return HttpResponse(f"{del_movie} was deleted!")
