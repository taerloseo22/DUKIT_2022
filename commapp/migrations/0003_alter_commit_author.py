# Generated by Django 4.1 on 2022-08-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commapp', '0002_commit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='author',
            field=models.TextField(max_length=50),
        ),
    ]