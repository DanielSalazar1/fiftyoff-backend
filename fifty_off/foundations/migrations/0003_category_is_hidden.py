# Generated by Django 2.2.6 on 2019-12-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0002_auto_20191204_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_hidden',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
