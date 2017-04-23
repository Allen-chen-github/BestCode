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
            name='PrimaryDepartment',
            fields=[
                ('primary_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('programming_language_id', models.AutoField(primary_key=True, serialize=False)),
                ('language_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryDepartment',
            fields=[
                ('secondary_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='./upload/users/photo')),
                ('primary_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PrimaryDepartment')),
                ('programming_languages', models.ManyToManyField(to='users.ProgrammingLanguage')),
                ('secondary_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SecondaryDepartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]