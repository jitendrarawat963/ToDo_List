# Generated by Django 4.1.6 on 2024-02-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]