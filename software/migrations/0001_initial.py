# Generated by Django 4.0.1 on 2022-01-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_title', models.CharField(max_length=50)),
                ('software_tutorial_link', models.CharField(max_length=200)),
                ('software_download_link', models.CharField(max_length=200)),
            ],
        ),
    ]
