# Generated by Django 4.2.6 on 2023-10-18 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("APARTMENT", "APARTMENT"),
                            ("VILLA HOUSE", "VILLA HOUSE"),
                            ("PENTHOUSE", "PENTHOUSE"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField()),
                ("address", models.CharField(max_length=200)),
                ("bedroom", models.IntegerField()),
                ("bathroom", models.IntegerField()),
                ("area", models.IntegerField()),
                ("floor", models.IntegerField()),
                ("parking", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "categoty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.category",
                    ),
                ),
            ],
        ),
    ]
