# Generated by Django 5.0.6 on 2024-07-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video_app", "0011_remove_media_file_alter_media_image_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="is_paused",
            field=models.BooleanField(default=False),
        ),
    ]
