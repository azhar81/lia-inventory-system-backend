# Generated by Django 4.1.1 on 2022-11-13 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspections', '0004_alter_inspection_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='inspector',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
