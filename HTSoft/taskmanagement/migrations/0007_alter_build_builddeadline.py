# Generated by Django 3.2.5 on 2023-08-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0006_auto_20230829_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='BuildDeadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
