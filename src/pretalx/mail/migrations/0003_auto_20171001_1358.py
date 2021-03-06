# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_queuedmail_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='subject',
            field=i18nfield.fields.I18nCharField(max_length=200, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='mailtemplate',
            name='text',
            field=i18nfield.fields.I18nTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='bcc',
            field=models.CharField(blank=True, help_text='One email address or several addresses separated by commas.', max_length=1000, null=True, verbose_name='BCC'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='cc',
            field=models.CharField(blank=True, help_text='One email address or several addresses separated by commas.', max_length=1000, null=True, verbose_name='CC'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='reply_to',
            field=models.CharField(blank=True, help_text='By default, the orga address is used as Reply-To.', max_length=1000, null=True, verbose_name='Reply-To'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='sent',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Sent at'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='queuedmail',
            name='to',
            field=models.CharField(help_text='One email address or several addresses separated by commas.', max_length=1000, verbose_name='To'),
        ),
    ]
