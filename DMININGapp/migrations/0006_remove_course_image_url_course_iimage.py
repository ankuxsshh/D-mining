# Generated by Django 5.2.1 on 2025-06-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMININGapp', '0005_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image_url',
        ),
        migrations.AddField(
            model_name='course',
            name='iimage',
            field=models.ImageField(blank=True, null=True, upload_to='static/courses/'),
        ),
    ]
