# Generated by Django 3.1.5 on 2021-07-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin', '0002_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='pincode',
            field=models.IntegerField(default=None, max_length=6),
        ),
        migrations.AlterField(
            model_name='filter',
            name='vaccine_name',
            field=models.CharField(choices=[('covaxin', 'Covaxin'), ('covishield', 'CoviShield'), ('sputnik', 'Sputnik')], default=None, max_length=100),
        ),
    ]