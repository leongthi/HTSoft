# Generated by Django 3.2.5 on 2023-08-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0005_auto_20230829_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildID', models.IntegerField()),
                ('ClientID', models.IntegerField()),
                ('BuildName', models.CharField(max_length=100)),
                ('BuildStatus', models.CharField(max_length=100)),
                ('BuildDeadline', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketCustomer',
        ),
    ]