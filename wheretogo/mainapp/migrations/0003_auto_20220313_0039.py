# Generated by Django 3.2.12 on 2022-03-12 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_organization_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationhashtag',
            name='food',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='еда'),
        ),
        migrations.AddField(
            model_name='userhashtag',
            name='food',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='еда'),
        ),
    ]
