# Generated by Django 4.0.1 on 2022-01-28 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_link',
            new_name='course_tutorial_link',
        ),
    ]
