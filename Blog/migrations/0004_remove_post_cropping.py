# Generated by Django 3.1 on 2020-08-15 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_cropping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cropping',
        ),
    ]