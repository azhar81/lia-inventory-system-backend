# Generated by Django 4.1.1 on 2022-11-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lend',
            name='status',
            field=models.IntegerField(choices=[(1, 'Berjalan'), (2, 'Ditutup')], default=1),
        ),
    ]
