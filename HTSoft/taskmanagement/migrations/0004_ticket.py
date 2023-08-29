# Generated by Django 3.2.5 on 2023-08-29 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
        ('taskmanagement', '0003_delete_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Priority', models.CharField(blank=True, max_length=50)),
                ('Status', models.CharField(blank=True, max_length=50)),
                ('DueDate', models.DateTimeField()),
                ('AssignedTo', models.IntegerField()),
                ('Title', models.CharField(blank=True, max_length=1000)),
                ('Description', models.CharField(blank=True, max_length=3000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, max_length=100)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=100)),
                ('Category', models.CharField(blank=True, max_length=300)),
                ('MODULE', models.CharField(blank=True, max_length=300)),
                ('PrimaryDEV', models.IntegerField()),
                ('PrimaryQC', models.IntegerField()),
                ('PrimaryBA', models.IntegerField()),
                ('TicketOwner', models.IntegerField()),
                ('Build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_Build_2Build', to='taskmanagement.build')),
                ('TicketCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_Customer_2TicketCustomer', to='shared.customer')),
            ],
        ),
    ]