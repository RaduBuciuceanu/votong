# Generated by Django 2.2.19 on 2021-03-17 09:11

import ckeditor_uploader.fields
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0036_auto_20210316_1743"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=254, verbose_name="Title")),
                ("slug", models.SlugField(unique=True)),
                ("author", models.CharField(max_length=100, verbose_name="Author")),
                ("content_preview", models.TextField(verbose_name="Content preview")),
                ("content", ckeditor_uploader.fields.RichTextUploadingField(verbose_name="Content")),
                ("is_visible", models.BooleanField(default=False, verbose_name="Is visible?")),
                ("published_date", models.DateField(blank=True, null=True, verbose_name="Date published")),
            ],
            options={"verbose_name": "Blog post", "verbose_name_plural": "Blog posts",},
        ),
    ]
