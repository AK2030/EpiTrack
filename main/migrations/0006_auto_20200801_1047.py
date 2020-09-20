

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200729_1722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 10, 47, 39, 766277), verbose_name='date published'),
        ),
    ]
