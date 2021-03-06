# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-02 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hobby.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='제품 카테고리')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='카테고리 설명')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('image', hobby.fields.ThumbnailImageField(upload_to='hobby/%Y/%m')),
                ('description', models.TextField(blank=True, verbose_name='제품 설명')),
                ('price', models.CharField(max_length=50, null=True, verbose_name='가격')),
                ('curator', models.CharField(max_length=50, null=True, verbose_name='큐레이터')),
                ('dliv_price', models.CharField(max_length=50, null=True, verbose_name='배송비')),
                ('buy', models.CharField(max_length=50, null=True, verbose_name='구매혜택')),
                ('buy_limit', models.CharField(max_length=50, null=True, verbose_name='구매제한')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 일시')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobby.Album')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
