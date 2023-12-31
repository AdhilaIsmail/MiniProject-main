# Generated by Django 4.2.4 on 2023-09-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_donor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('blood_group', models.CharField(max_length=5)),
                ('place', models.CharField(max_length=100)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
