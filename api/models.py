from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db.models import UniqueConstraint

# creating model Movie
class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=365)
    
    # add field "number of ratings"
    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    # add field "average rating"
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    # Add name of object when showing in admin page
    def __str__(self):
        return self.title

# creating model Rating
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # create primary key for table 
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
        # we can also use 2 following lines beacause 2 previous line maybe outdate
        # UniqueConstraint(fields=['user', 'movie'], name='unique_rating'),
        # models.Index(fields=['user', 'movie'])
    
    # Add name of object when showing in admin page
    def __str__(self):
        return self.movie, self.stars