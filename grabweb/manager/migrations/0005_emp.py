# Generated by Django 4.2.3 on 2023-08-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Name', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('empid', models.CharField(max_length=30)),
            ],
        ),
    ]
