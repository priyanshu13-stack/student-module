# Generated by Django 4.1.4 on 2023-03-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_sample_allottedcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='appno',
            field=models.CharField(default=False, max_length=200, unique=True),
        ),
    ]
