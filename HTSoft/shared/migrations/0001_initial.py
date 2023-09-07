# Generated by Django 3.2.5 on 2023-09-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_main', models.IntegerField(blank=True, null=True)),
                ('Responsibility', models.CharField(blank=True, max_length=255, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('UserName', models.CharField(blank=True, max_length=255, null=True)),
                ('PASSWORD', models.CharField(blank=True, max_length=255, null=True)),
                ('IsActive', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
