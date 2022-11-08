# Generated by Django 4.1.1 on 2022-11-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=50)),
                ("about", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("IT", "IT"),
                            ("Non IT", "Non IT"),
                            ("Mobile Phone", "Mobile Phone"),
                        ],
                        max_length=100,
                    ),
                ),
                ("added_date", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
