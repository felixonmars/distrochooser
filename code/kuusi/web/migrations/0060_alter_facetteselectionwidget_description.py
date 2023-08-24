# Generated by Django 4.2.4 on 2023-08-24 07:47

from django.db import migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0059_facetteselectionwidget_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facetteselectionwidget",
            name="description",
            field=web.models.TranslateableField(
                blank=True,
                default=None,
                help_text="A comment for translators to identify this value",
                max_length=250,
                null=True,
            ),
        ),
    ]
