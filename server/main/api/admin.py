from django.contrib import admin
from .models import Movie

class MoviesAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'description', 'genre']
admin.site.register(Movie, MoviesAdmin)


