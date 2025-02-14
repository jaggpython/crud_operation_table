# Generated by Django 4.2.5 on 2024-09-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=30)),
                (
                    "branch",
                    models.CharField(
                        choices=[
                            ("CS", "Computer Science"),
                            ("EC", "Electronics and Communication"),
                            ("ME", "Mechanical Engineering"),
                            ("CE", "Civil Engineering"),
                        ],
                        default="CS",
                        max_length=100,
                    ),
                ),
                ("register_num", models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
