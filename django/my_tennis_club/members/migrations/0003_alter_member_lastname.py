# Generated by Django 5.0.3 on 2024-03-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
    ]
