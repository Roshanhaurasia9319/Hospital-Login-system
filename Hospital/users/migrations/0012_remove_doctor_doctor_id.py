# Generated by Django 5.0.7 on 2024-07-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_doctor_doctor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_id',
        ),
    ]
