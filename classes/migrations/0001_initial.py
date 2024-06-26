# Generated by Django 5.0.6 on 2024-06-25 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestClasses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'request_classes',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(choices=[('BIO', 'Biology'), ('MATH', 'Mathematics'), ('CHEM', 'Chemistry'), ('PHYSC', 'Physics'), ('ENG', 'English')], max_length=8)),
                ('class_level', models.CharField(choices=[('HS', 'High School'), ('UNI', 'University')], max_length=3)),
                ('value_by_hour', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers')),
            ],
            options={
                'db_table': 'classes',
                'ordering': ['created_at'],
            },
        ),
    ]
