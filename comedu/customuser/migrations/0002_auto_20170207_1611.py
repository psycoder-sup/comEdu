# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='position',
            field=models.CharField(choices=[('pro', '교수'), ('stu', '학생')], default='학생', max_length=10, verbose_name='직책(교수, 학생)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='student_id',
            field=models.IntegerField(default=0, unique=True, verbose_name='student_id(학번)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='', max_length=20, verbose_name='name'),
            preserve_default=False,
        ),
    ]
