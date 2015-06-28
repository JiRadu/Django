# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150625_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='/media', default=datetime.datetime(2015, 6, 25, 12, 45, 31, 198094, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
