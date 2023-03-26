# Generated by Django 4.1.4 on 2023-03-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='allottedcategory',
            field=models.CharField(choices=[('HS', 'HS'), ('OS', 'OS'), ('AI', 'AI')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='sample',
            name='allottedquota',
            field=models.CharField(choices=[('OPNO', 'OPNO'), ('SCNO', 'SCNO'), ('STNO', 'STNO'), ('NODF', 'NODF'), ('NOPH', 'NOPH')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='sample',
            name='category',
            field=models.CharField(choices=[('GN', 'GN'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('EWS', 'EWS'), ('AICTE', 'AICTE')], default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='sample',
            name='emailid',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sample',
            name='enrollmentno',
            field=models.IntegerField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='sample',
            name='region',
            field=models.CharField(choices=[('DELHI', 'DELHI'), ('OUTSIDE DELHI', 'OUTSIDE DELHI')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='sample',
            name='stream',
            field=models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE')], default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='sample',
            name='subcategory',
            field=models.CharField(choices=[('DEFENCE', 'DEFENCE'), ('JAIN', 'JAIN'), ('MUSLIM', 'MUSLIM'), ('SIKH', 'SIKH'), ('PWD', 'PWD'), ('JK', 'JK')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='sample',
            name='type',
            field=models.CharField(choices=[('REGULAR', 'REGULAR'), ('UPGRADED', 'UPGRADED'), ('LE', 'LE')], default='Regular', max_length=10),
        ),
    ]
