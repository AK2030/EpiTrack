

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200712_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='disease_added',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 17, 22, 17, 549721), verbose_name='date published'),
        ),
    ]
