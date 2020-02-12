from django.contrib import admin
from .models import Movie, Rating

# add Movie, Rating field into admin page
admin.site.register(Movie)
admin.site.register(Rating)