# Generated by Django 5.1.1 on 2024-10-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]
