# Generated by Django 3.1.7 on 2023-02-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-08-20'),
            preserve_default=False,
        ),
    ]
