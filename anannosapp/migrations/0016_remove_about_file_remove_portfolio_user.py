# Generated by Django 4.2.5 on 2023-09-13 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anannosapp', '0015_remove_portfolio_image_remove_portfolio_video_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='file',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='user',
        ),
    ]
