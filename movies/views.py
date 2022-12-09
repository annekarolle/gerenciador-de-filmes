
from rest_framework.views import APIView, Request, Response, status

from kenzie_buster.pagination import CustomPageNumberPagination
from .serializers import MovieOrderSerializer, MovieSerializer
from django.shortcuts import get_object_or_404

from .models import Movie

from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb

from users.permissions import Authenticated, IsAdminOrReadOnly
# Create your views here.


class MovieView(APIView, CustomPageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)



class MovieViewDetail(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class OrderMovieView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [Authenticated]

    def post(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)
        self.check_object_permissions(request, movie)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
