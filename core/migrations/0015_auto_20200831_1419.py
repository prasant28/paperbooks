# Generated by Django 2.2.14 on 2020-08-31 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_auto_20200830_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
