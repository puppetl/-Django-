# Generated by Django 2.2.8 on 2020-03-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juheapp', '0002_auto_20200228_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cithabc',
            field=models.TextField(default=[]),
        ),
    ]