# Generated by Django 4.2.4 on 2023-08-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0056_sessionversionwidget"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="in_versions",
            field=models.ManyToManyField(blank=True, to="web.sessionversion"),
        ),
    ]
