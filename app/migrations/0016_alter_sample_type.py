# Generated by Django 4.1.1 on 2022-12-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_sample_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='type',
            field=models.CharField(choices=[('regular', 'REGULAR'), ('upgraded', 'UPGRADED'), ('le', 'LE')], default='Regular', max_length=10),
        ),
    ]
