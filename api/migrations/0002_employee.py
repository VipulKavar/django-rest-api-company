# Generated by Django 4.1.1 on 2022-11-08 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                ("about", models.TextField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Manager", "Manager"),
                            ("Software Developer", "sd"),
                            ("Project Leader", "pl"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]
