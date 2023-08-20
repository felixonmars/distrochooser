# Generated by Django 4.2.4 on 2023-08-20 06:45

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0033_session_result_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="result_id",
            field=models.CharField(
                default=web.models.get_session_result_id, max_length=10
            ),
        ),
    ]
