# Generated by Django 4.0.5 on 2022-06-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0006_coursemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='payefeesmodel',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]