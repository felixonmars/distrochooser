# Generated by Django 3.2.18 on 2023-03-26 10:11

import distrochooser.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0096_answerdistributionmatrix_isnegativesuggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSuggestionSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionToken', models.CharField(default=distrochooser.models.get_token, max_length=200)),
            ],
        ),
    ]
