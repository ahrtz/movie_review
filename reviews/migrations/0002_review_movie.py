# Generated by Django 2.2.7 on 2020-06-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_moviecomment'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
            preserve_default=False,
        ),
    ]