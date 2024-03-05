# Generated by Django 5.0.2 on 2024-02-21 12:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_register_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='course_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'date__gte': datetime.datetime(2024, 2, 21, 12, 13, 51, 214147, tzinfo=datetime.timezone.utc)}, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.exam_details'),
        ),
    ]
