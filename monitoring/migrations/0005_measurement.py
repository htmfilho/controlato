# Generated by Django 3.0.4 on 2020-03-22 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0004_indicator_formula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField()),
                ('used_formula', models.CharField(blank=True, max_length=255, null=True)),
                ('filled_formula', models.CharField(blank=True, max_length=255, null=True)),
                ('measurement_date', models.DateTimeField()),
                ('record_date', models.DateTimeField(auto_now=True)),
                ('indicator_context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.IndicatorContext')),
            ],
        ),
    ]
