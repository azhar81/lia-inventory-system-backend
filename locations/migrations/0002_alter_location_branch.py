# Generated by Django 4.1.1 on 2022-12-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='branch',
            field=models.CharField(choices=[('CKL', 'Cikokol'), ('KRC', 'Karawaci'), ('BSD', 'BSD')], max_length=3),
        ),
    ]
