# Generated by Django 2.0.6 on 2018-09-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0036_auto_20180906_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultindicatorperiodactualdimension',
            name='result_indicator_period',
        ),
        migrations.AddField(
            model_name='resultindicatorperiodactualdimension',
            name='result_indicator_period_actual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iati.ResultIndicatorPeriodActual'),
        ),
    ]
