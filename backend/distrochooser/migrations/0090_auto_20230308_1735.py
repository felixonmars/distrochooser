# Generated by Django 3.2.18 on 2023-03-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0089_answerdistributionmatrix_issuggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='answerdistributionmatrix',
            name='suggestions',
            field=models.ManyToManyField(blank=True, related_name='suggestion_matrix', to='distrochooser.AnswerDistributionMatrix'),
        ),
    ]