# Generated by Django 5.0.4 on 2024-05-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210629_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='span',
            field=models.TextField(blank=True, null=True),
        ),
    ]
