# Generated by Django 2.1.8 on 2021-06-13 21:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20210613_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='users_unlike',
            field=models.ManyToManyField(blank=True, related_name='articles_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]