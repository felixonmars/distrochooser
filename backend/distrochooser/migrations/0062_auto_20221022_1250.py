# Generated by Django 2.2.28 on 2022-10-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0061_answer_peculiarities'),
    ]

    operations = [
        migrations.CreateModel(
            name='GivenPeculiarities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pecularities', models.TextField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distrochooser.UserSession')),
            ],
        ),
        migrations.AddIndex(
            model_name='givenpeculiarities',
            index=models.Index(fields=['session'], name='distrochoos_session_beed58_idx'),
        ),
    ]
