# Generated by Django 4.2.4 on 2023-08-19 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0016_page_next_page_page_previous_page"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="page",
            name="previous_page",
        ),
    ]