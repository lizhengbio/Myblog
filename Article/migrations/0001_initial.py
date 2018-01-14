# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\x96\x87\xe5\xad\x97\xe6\xa0\x87\xe9\xa2\x98')),
                ('date', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('tag', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
                ('short_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('src', models.CharField(max_length=64)),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
    ]
