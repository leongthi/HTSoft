# Generated by Django 3.2.5 on 2023-09-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='map_user_ticket',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
