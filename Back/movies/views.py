from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .serializers.movie import MovieListSerializer, MovieSerializer, MovieGenreListSerializer
from .serializers.actor import ActorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def movieList_info(request):
    movielist = get_list_or_404(Movie)
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    # for similar_movie_id in serializer.data.get('movie_similar'):
    #     print(similar_movie_id)
        # similar_movie = get_object_or_404(Movie, pk=similar_movie_id)
        # similar_serializer = MovieListSerializer(similar_movie)
        # print(similar_serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def genre_list(request, q):
    
    results = Movie.objects.filter(title__icontains = q.replace(" ", ""))
    serializer = MovieGenreListSerializer(results, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)