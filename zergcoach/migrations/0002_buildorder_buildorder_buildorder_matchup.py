# Generated by Django 4.2.1 on 2023-05-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zergcoach', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildorder',
            name='buildorder',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='buildorder',
            name='matchup',
            field=models.CharField(default='', max_length=120),
        ),
    ]