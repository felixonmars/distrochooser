# Generated by Django 3.2.18 on 2023-03-12 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0092_alter_usersuggestion_old_mapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersuggestion',
            name='new_mapping',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_Suggestion_New', to='distrochooser.answerdistributionmatrix'),
        ),
    ]
