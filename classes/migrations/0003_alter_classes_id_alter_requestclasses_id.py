# Generated by Django 5.0.6 on 2024-06-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='requestclasses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]