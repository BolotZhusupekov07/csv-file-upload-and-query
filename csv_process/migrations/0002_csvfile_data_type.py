# Generated by Django 5.0.6 on 2024-07-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csv_process", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="csvfile",
            name="data_type",
            field=models.CharField(
                choices=[("CITIES", "Cities")], default="CITIES", max_length=20
            ),
        ),
    ]