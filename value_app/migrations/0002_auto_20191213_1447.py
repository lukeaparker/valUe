# Generated by Django 3.0 on 2019-12-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('value_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='tag',
            field=models.TextField(help_text='Enter a value tag', unique=True),
        ),
    ]