# Generated by Django 4.1.1 on 2022-12-13 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_sample_yearofadmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='sno',
        ),
    ]
