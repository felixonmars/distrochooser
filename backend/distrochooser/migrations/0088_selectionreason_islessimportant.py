# Generated by Django 4.1.4 on 2023-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("distrochooser", "0087_givenanswer_islessimportant"),
    ]

    operations = [
        migrations.AddField(
            model_name="selectionreason",
            name="isLessImportant",
            field=models.BooleanField(default=False),
        ),
    ]
