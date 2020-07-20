# Generated by Django 3.0.8 on 2020-07-20 13:47

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_answer_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name=users.models.User),
        ),
    ]