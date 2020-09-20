

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200801_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(choices=[('Coronavirus', 'Coronavirus'), ('Salmonella', 'Salmonella'), ('Common cold', 'Common col'), ('Flu', 'Flu')], default='coronavirus', max_length=20),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 12, 10, 29, 119700), verbose_name='date published'),
        ),
    ]
