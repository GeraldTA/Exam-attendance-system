# Generated by Django 5.0.2 on 2024-02-20 12:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('year_taken', models.IntegerField()),
                ('department_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=300)),
                ('surname', models.CharField(max_length=300)),
                ('program', models.CharField(max_length=300, null=True)),
                ('year', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('number_of_students', models.IntegerField()),
                ('invigilator', models.CharField(max_length=300)),
                ('course_id', models.ForeignKey(limit_choices_to={'year_taken': 2024}, on_delete=django.db.models.deletion.CASCADE, to='students.course_details')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField(default=False)),
                ('signature', models.TextField(default='In prgress, comming soon', max_length=100)),
                ('course_id', models.ForeignKey(blank=True, limit_choices_to={'date__gte': datetime.datetime(2024, 2, 20, 12, 38, 43, 836217, tzinfo=datetime.timezone.utc)}, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.exam_details')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student_details')),
            ],
        ),
    ]
