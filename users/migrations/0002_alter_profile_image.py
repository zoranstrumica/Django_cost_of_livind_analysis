# Generated by Django 5.1.3 on 2024-12-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_pics/default.jpg", upload_to="profile_pics"
            ),
        ),
    ]
