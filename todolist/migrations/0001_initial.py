# Generated by Django 3.0.1 on 2020-01-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=400)),
                ('check', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'todolists',
            },
        ),
    ]
