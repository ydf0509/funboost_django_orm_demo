# Generated by Django 3.2.13 on 2024-01-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=10)),
            ],
        ),
    ]
