# Generated by Django 4.2.3 on 2024-01-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_hashtags_hashtag_rename_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='movie',
            name='hashtag',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=None),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='HashTag',
        ),
    ]