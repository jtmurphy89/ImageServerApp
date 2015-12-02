# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imageUploader.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMGFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=imageUploader.models.generate_filename)),
            ],
        ),
    ]
