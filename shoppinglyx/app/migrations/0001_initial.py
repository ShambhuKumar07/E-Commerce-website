# Generated by Django 5.0.4 on 2024-04-18 07:36

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
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("selling_price", models.FloatField()),
                ("discounted_price", models.FloatField()),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("M", "Mobile"),
                            ("L", "Laptop"),
                            ("TW", "Top Wear"),
                            ("BW", "Bottom Wear"),
                        ],
                        max_length=2,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("zipcode", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Andhra Pradesh", "Andhra Pradesh"),
                            ("Arunachal Pradesh", "Arunachal Pradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Chhattisgarh", "Chhattisgarh"),
                            ("Goa", "Goa"),
                            ("Gujarat", "Gujarat"),
                            ("Haryana", "Haryana"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                            ("Jharkhand", "Jharkhand"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Maharashtra", "Maharashtra"),
                            ("Manipur", "Manipur"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Nagaland", "Nagaland"),
                            ("Odisha", "Odisha"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Sikkim", "Sikkim"),
                            ("Tamil Nadu", "Tamil Nadu"),
                            ("Telangana", "Telengana"),
                            ("Tripura", "Tripura"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Uttarakhand", "Uttarakhand"),
                            ("West Bengal", "West Bengal"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On the way", "On the way"),
                            ("Delivered", "Delivered"),
                            ("Cancel", "Cancel"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                (
                    "Customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
    ]