# Generated by Django 4.1.4 on 2022-12-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
