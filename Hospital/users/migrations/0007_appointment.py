# Generated by Django 5.0.7 on 2024-07-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_category_doctorblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Speciality', models.CharField(max_length=500)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
    ]
