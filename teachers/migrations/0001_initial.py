# Generated by Django 5.0.6 on 2024-06-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=320)),
                ('subjects', models.CharField(max_length=320)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
