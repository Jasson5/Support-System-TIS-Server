# Generated by Django 3.2.8 on 2021-11-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211123_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterPassword',
            field=models.CharField(default='y8uo0M3kCczEWg6', max_length=20),
        ),
    ]