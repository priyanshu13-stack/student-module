# Generated by Django 4.1.1 on 2022-10-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_dob_sample_dob_rename_stream_sample_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='appno',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
