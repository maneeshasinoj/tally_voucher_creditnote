# Generated by Django 4.0.4 on 2022-10-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_receiptvoucher_particulars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance6',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance7',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentvoucher',
            name='curbalance8',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance6',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance7',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiptvoucher',
            name='curbalance8',
            field=models.IntegerField(null=True),
        ),
    ]