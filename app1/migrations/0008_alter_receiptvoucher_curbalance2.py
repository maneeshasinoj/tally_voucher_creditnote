# Generated by Django 4.0.4 on 2022-10-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_paymentvoucher_curbalance2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptvoucher',
            name='curbalance2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]