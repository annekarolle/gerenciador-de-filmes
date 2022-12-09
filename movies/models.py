from django.db import models

# Create your models here.


class Rating(models.TextChoices):
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(null=True, max_length=20)
    rating = models.CharField(
        max_length=20,
        choices=Rating.choices,
        default=Rating.DEFAULT
    )
    synopsis = models.TextField(null=True)
    user = models.ForeignKey(
        "users.User", related_name="movie", on_delete=models.CASCADE, default=None)

    def __repr__(self) -> str:
        return f"Movie - title:{self.title} - id:{self.id}"


class Order(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order",
    )


def __repr__(self) -> str:
    return f"Order Movie -[{self.id}] title:{self.movie.title} price:{self.price} - "
