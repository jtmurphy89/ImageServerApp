# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageUploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgfile',
            old_name='img',
            new_name='imgFile',
        ),
    ]
