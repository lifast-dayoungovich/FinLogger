# Generated by Django 3.1.6 on 2021-02-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]