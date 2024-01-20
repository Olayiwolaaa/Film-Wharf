from django.urls import path
from .views import MovieView, SearchMovieView

urlpatterns = [
    path('api', MovieView.as_view(), name='home'),
    path('search', SearchMovieView.as_view(), name='search'),
]
