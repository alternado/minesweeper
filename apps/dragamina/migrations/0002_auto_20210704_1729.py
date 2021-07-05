# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-04 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragamina', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameboard',
            old_name='fecha_creacion',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='gameboard',
            old_name='fecha_actualizacion',
            new_name='update_date',
        ),
        migrations.RemoveField(
            model_name='gameboard',
            name='estado',
        ),
        migrations.AddField(
            model_name='gameboard',
            name='status',
            field=models.IntegerField(choices=[(1, 'Activate'), (0, 'Deactivate')], default=1),
        ),
    ]
