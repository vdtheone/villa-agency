# Generated by Django 4.2.6 on 2023-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_rename_imgage_property_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
