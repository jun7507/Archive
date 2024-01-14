# Generated by Django 5.0 on 2024-01-12 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BookList",
            fields=[
                (
                    "bcode",
                    models.IntegerField(
                        db_column="BCODE", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(db_column="TITLE", max_length=200)),
                (
                    "author",
                    models.CharField(
                        blank=True, db_column="AUTHOR", max_length=20, null=True
                    ),
                ),
                (
                    "year_of_publication",
                    models.CharField(
                        blank=True,
                        db_column="YEAR-OF-PUBLICATION",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "price",
                    models.IntegerField(blank=True, db_column="PRICE", null=True),
                ),
            ],
            options={
                "db_table": "book_list",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BookStore",
            fields=[
                (
                    "bscode",
                    models.IntegerField(
                        db_column="BSCODE", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_column="NAME", max_length=100)),
                (
                    "tel",
                    models.CharField(
                        blank=True, db_column="TEL", max_length=15, null=True
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, db_column="COUNTRY", max_length=20, null=True
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, db_column="CITY", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "db_table": "book_store",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                ("subject", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
                ("modify_date", models.DateTimeField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_question",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "voter",
                    models.ManyToManyField(
                        related_name="voter_question", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
                ("modify_date", models.DateTimeField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_answer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "voter",
                    models.ManyToManyField(
                        related_name="voter_answer", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="adul.question"
                    ),
                ),
            ],
        ),
    ]