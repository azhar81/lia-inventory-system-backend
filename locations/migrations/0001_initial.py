# Generated by Django 4.1.1 on 2022-11-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CKL', 'Cikokol'), ('TGR', 'Tanggerang'), ('BSD', 'BSD')], max_length=3)),
                ('floor', models.CharField(max_length=2)),
                ('room', models.CharField(max_length=10)),
            ],
        ),
    ]
