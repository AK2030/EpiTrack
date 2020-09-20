

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200801_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('coronavirus', 'CORONAVIRUS'), ('salmonella', 'SALMONELLA'), ('common cold', 'COMMON COLD'), ('flu', 'FLU')], default='coronavirus', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 11, 2, 19, 311647), verbose_name='date published'),
        ),
    ]
