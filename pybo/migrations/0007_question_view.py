# Generated by Django 3.1.3 on 2022-06-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20220524_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
