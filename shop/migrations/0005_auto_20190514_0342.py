# Generated by Django 2.2.1 on 2019-05-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190513_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='battery',
            field=models.CharField(blank=True, default='', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='behind_camera',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cpu',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='front_camera',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gpu',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='monitor',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='op_sys',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rom',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
