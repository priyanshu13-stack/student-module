# Generated by Django 4.1.4 on 2023-05-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_sample_admitted_alter_sample_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='admitted',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='management',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='', max_length=50, null=True),
        ),
    ]
