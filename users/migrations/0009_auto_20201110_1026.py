# Generated by Django 3.0.8 on 2020-11-10 10:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_elective_semester'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='elective',
            unique_together={('user', 'elective', 'semester')},
        ),
    ]
