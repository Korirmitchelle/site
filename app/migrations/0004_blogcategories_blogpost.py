# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 16:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'live'), (2, 'draft'), (3, 'hidden')], default=1)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('image1', models.ImageField(upload_to='images', verbose_name='Images')),
                ('image2', models.ImageField(blank=True, upload_to='images', verbose_name='Images')),
                ('image3', models.ImageField(blank=True, upload_to='images', verbose_name='Images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BlogCategories')),
            ],
            options={
                'ordering': ['pub_date'],
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'blog posts',
            },
        ),
    ]
