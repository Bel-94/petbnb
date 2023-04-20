# Generated by Django 4.1.3 on 2023-04-20 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardingService",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="pets.service",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Boarding Services",
            },
            bases=("pets.service",),
        ),
        migrations.CreateModel(
            name="GroomingService",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="pets.service",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Grooming Services",
            },
            bases=("pets.service",),
        ),
        migrations.CreateModel(
            name="Payment",
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
                    "transaction_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("transaction_date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Payments",
            },
        ),
        migrations.CreateModel(
            name="VeterinaryService",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="pets.service",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Veterinary Services",
            },
            bases=("pets.service",),
        ),
        migrations.AlterModelOptions(
            name="pet",
            options={"verbose_name_plural": "Pets"},
        ),
        migrations.AlterModelOptions(
            name="serviceprovider",
            options={"verbose_name_plural": "ServiceProviders"},
        ),
        migrations.AddField(
            model_name="pet",
            name="age",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="pet",
            name="breed",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="pet",
            name="category",
            field=models.CharField(default="unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="pet",
            name="gender",
            field=models.CharField(default="unknown", max_length=10),
        ),
        migrations.AddField(
            model_name="pet",
            name="medical_history",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="pet",
            name="name",
            field=models.CharField(default="unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="availability",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="capacity",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="contact_info",
            field=models.CharField(default="example@example.com", max_length=255),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="booking",
            name="pet_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="PetOwner",
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="BoardingService",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="pets.boardingservice",
            ),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="GroomingService",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="pets.groomingservice",
            ),
        ),
        migrations.AddField(
            model_name="serviceprovider",
            name="VeterinaryService",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="pets.veterinaryservice",
            ),
        ),
    ]
