# Generated by Django 4.2.4 on 2023-08-19 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0027_facette_is_exclusive"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facette",
            name="is_exclusive",
        ),
    ]
