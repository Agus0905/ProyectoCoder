# Generated by Django 4.0.3 on 2022-03-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id',
        ),
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
