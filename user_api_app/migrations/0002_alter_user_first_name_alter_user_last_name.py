# Generated by Django 5.0.6 on 2024-06-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
