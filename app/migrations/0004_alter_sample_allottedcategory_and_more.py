# Generated by Django 4.1.4 on 2023-04-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_sample_appno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='allottedcategory',
            field=models.CharField(choices=[('OPNO', 'OPNO'), ('SCNO', 'SCNO'), ('NODF', 'NODF')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='sample',
            name='allottedquota',
            field=models.CharField(choices=[('HS', 'HS'), ('OS', 'OS'), ('AI', 'AI')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='sample',
            name='type',
            field=models.CharField(choices=[('REGULAR', 'REGULAR'), ('UPGRADED', 'UPGRADED'), ('LE', 'LE'), ('MANAGEMENT', 'MANAGEMENT')], default='Regular', max_length=10),
        ),
    ]
