# Generated by Django 3.2.5 on 2023-08-29 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildName', models.CharField(max_length=100)),
                ('BuildDeadline', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('BuildCustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_Customer_2BuildCustomerID', to='shared.customer')),
                ('BuildStatusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_Status_2BuildStatusID', to='shared.status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Build_2created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Build_2modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
