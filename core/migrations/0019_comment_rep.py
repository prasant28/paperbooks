# Generated by Django 2.2.14 on 2020-09-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200901_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rep',
            field=models.TextField(blank=True, null=True),
        ),
    ]
