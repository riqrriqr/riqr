# Generated by Django 3.2.8 on 2021-12-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='activation_date',
            field=models.DateTimeField(null=True, verbose_name='Дата создания'),
        ),
    ]