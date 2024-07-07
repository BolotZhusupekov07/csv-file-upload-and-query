# Generated by Django 5.0.6 on 2024-07-07 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("csv_process", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("population", models.IntegerField()),
                ("established_at", models.DateTimeField()),
                (
                    "csv_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="csv_process.csvfile",
                    ),
                ),
            ],
        ),
    ]
