# Generated by Django 3.2.8 on 2021-11-30 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_semester_semesterpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterPassword',
            field=models.CharField(default='nLidrxU4hlrKRN8', max_length=20),
        ),
    ]
