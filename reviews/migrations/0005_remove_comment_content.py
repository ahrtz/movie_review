# Generated by Django 2.1.15 on 2020-06-16 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_comment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
    ]
