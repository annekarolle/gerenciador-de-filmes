from rest_framework import serializers
from .models import Order, Rating, Movie
import ipdb



class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, required=True)
    duration = serializers.CharField(
        max_length=20, default=None, required=False)
    rating = serializers.ChoiceField(
        choices=Rating.choices,
        default=Rating.DEFAULT,
        required=False,
    )
    synopsis = serializers.CharField(required=False, default=None)

    added_by = serializers.SerializerMethodField(
        read_only=True, method_name='get_added_by')

    def get_added_by(self, data):
        return data.user.email

    def create(self, validated_data):
        usuario = validated_data.pop("user")
        movie, created = Movie.objects.get_or_create(
            **validated_data, user=usuario)

        return movie

    def update(self, instance, validated_data: dict,):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class MovieOrderSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(
        max_digits=8, decimal_places=2, required=True)

    buyed_by = serializers.SerializerMethodField(required=False)
    title = serializers.SerializerMethodField()

    def get_buyed_by(self, book):
        return book.user.email

    def get_title(self, book):
        return book.movie.title

    def create(self, validated_data: dict):
        order = Order.objects.create(**validated_data)

        return order
