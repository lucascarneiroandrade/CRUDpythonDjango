# Generated by Django 3.0.4 on 2020-03-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
