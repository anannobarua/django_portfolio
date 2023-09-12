# Generated by Django 4.2.5 on 2023-09-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anannosapp', '0004_project_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
