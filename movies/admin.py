from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    #fields = ("title", "genre")
    exclude = ('date_created',)
    list_display = ('title', 'release_year',
                    'number_in_stock', 'daily_rate', 'genre')


# Register your models herce.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
