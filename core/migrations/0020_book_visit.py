# Generated by Django 2.2.14 on 2020-09-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_comment_rep'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='visit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
