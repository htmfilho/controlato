# Generated by Django 3.0.4 on 2020-03-21 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Context',
            new_name='IndicatorContext',
        ),
    ]
