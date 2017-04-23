# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 01:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.IntegerField()),
                ('comment_time', models.DateTimeField(verbose_name='Comment Time')),
                ('comment_text', models.TextField(max_length=4096)),
                ('agree_count', models.IntegerField()),
                ('disagree_count', models.IntegerField()),
                ('reply_of_comment_id', models.IntegerField()),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentType',
            fields=[
                ('comment_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_type_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.CommentType'),
        ),
    ]