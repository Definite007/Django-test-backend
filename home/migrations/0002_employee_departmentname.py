# Generated by Django 4.0.5 on 2022-06-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='DepartmentName',
            field=models.CharField(default='IT', max_length=40),
        ),
    ]
