# Generated by Django 4.0.4 on 2022-10-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_receiptvoucher_curbalance2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptvoucher',
            name='curbalance2',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]
