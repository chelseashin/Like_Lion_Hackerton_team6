# Generated by Django 2.1.8 on 2019-11-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cigarettes', '0004_auto_20191110_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobacco',
            name='feel_of_hit',
            field=models.CharField(default='중', max_length=10),
        ),
    ]
