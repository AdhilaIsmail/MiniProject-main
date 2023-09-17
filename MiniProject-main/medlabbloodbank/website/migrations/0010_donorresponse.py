# Generated by Django 4.2.4 on 2023-09-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_delete_donorresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('bloodType', models.CharField(max_length=3)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('donorHistory', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('difficulty', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('donated', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('allergies', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('alcohol', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('jail', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('surgery', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('diseased', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('hivaids', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('pregnant', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True)),
                ('child', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True)),
                ('feelgood', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True)),
            ],
        ),
    ]