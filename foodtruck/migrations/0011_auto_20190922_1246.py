# Generated by Django 2.2.3 on 2019-09-22 03:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0010_merge_20190922_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruckcomment',
            name='ftCommentTimeStamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 3, 46, 48, 396353, tzinfo=utc)),
        ),
    ]
