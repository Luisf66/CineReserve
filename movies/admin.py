from django.contrib import admin
from .models import Movie


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('title', 'release_date', 'duration_minutes')

admin.site.register(Movie, MovieAdmin)
