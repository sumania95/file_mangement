# Generated by Django 3.1.6 on 2022-03-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20220307_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='remarks',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='series_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
