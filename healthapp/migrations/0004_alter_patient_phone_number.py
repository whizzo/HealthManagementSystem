# Generated by Django 4.0.10 on 2023-05-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0003_patient_confirm_password_patient_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
