# Generated by Django 3.2.8 on 2021-11-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_semester_semesterpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterPassword',
            field=models.CharField(default='zMkw4rgMAAo0a9y', max_length=20),
        ),
    ]
