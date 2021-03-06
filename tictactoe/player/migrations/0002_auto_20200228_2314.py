# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-28 23:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(help_text='Its always nice to add a friendly message', max_length=300, verbose_name='Optional Message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text='Please select the user you want to play the game with.', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]
