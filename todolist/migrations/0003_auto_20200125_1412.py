# Generated by Django 3.0.1 on 2020-01-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]