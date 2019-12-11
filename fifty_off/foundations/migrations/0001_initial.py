# Generated by Django 2.2.6 on 2019-12-04 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('percent_off', models.FloatField()),
                ('serial', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('photo', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('is_hidden', models.BooleanField(blank=True, default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundations.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundations.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
