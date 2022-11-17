# Generated by Django 4.1.1 on 2022-11-13 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('lends', '0002_lend_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lend',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.dynamicasset'),
        ),
    ]