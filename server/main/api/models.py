from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    genre = models.CharField(max_length=350, default=None)
    hashtag = models.CharField(max_length=350, default=None)
    download_link = models.CharField(max_length=1000)
    description = models.TextField()
    source = models.CharField(max_length=250, default="Nkiri")
    release_date = models.DateField(default=None, default=None)
    thumbnail_url = models.CharField(max_length=1000)
    Trailer_url = models.CharField(max_length=1000)
    director = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.name + " - " + str(self.genre)  # Display movie name and category name

