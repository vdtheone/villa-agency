# Generated by Django 4.2.6 on 2023-10-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="price",
            field=models.FloatField(),
        ),
    ]
