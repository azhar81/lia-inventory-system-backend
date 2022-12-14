# Generated by Django 4.1.1 on 2022-11-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0005_alter_inspection_inspector'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='ongoing',
            field=models.BooleanField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='photo',
            field=models.ImageField(upload_to='inspections/'),
        ),
    ]
