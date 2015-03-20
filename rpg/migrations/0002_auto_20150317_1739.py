# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rpg.models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='isover',
        ),
        migrations.RemoveField(
            model_name='game',
            name='stats',
        ),
        migrations.AddField(
            model_name='game',
            name='cmd',
            field=models.CharField(default=None, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='introduction',
            field=models.TextField(default=b'in the room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='items',
            field=rpg.models.ListField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='inventory',
            field=rpg.models.ListField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='session',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='exits',
            field=rpg.models.ListField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='items',
            field=rpg.models.ListField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='neighbors',
            field=rpg.models.ListField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default=b'player1', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
