# Generated by Django 4.0.10 on 2023-05-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_alter_appointment_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='confirm_password',
            field=models.CharField(blank=True, default='some_value', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(blank=True, default='some_value', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default=None, max_length=2),
        ),
    ]
