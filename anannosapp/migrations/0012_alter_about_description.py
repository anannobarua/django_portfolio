# Generated by Django 4.2.5 on 2023-09-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anannosapp', '0011_portfolio_delete_project_alter_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
