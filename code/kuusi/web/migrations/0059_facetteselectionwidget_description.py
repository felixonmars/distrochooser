# Generated by Django 4.2.4 on 2023-08-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0058_rename_in_versions_page_not_in_versions"),
    ]

    operations = [
        migrations.AddField(
            model_name="facetteselectionwidget",
            name="description",
            field=models.TextField(blank=True, default=None, max_length=250, null=True),
        ),
    ]