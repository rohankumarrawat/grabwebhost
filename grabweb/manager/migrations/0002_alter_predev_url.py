# Generated by Django 4.2.3 on 2023-07-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predev',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
