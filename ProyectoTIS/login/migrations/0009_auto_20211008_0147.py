# Generated by Django 3.2.8 on 2021-10-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20211008_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol',
            old_name='tipoDeRol',
            new_name='tipoRol',
        ),
        migrations.AlterField(
            model_name='rol',
            name='rolId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]