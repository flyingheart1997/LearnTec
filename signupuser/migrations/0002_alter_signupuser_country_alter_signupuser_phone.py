# Generated by Django 4.0.1 on 2022-01-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupuser',
            name='country',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='signupuser',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]