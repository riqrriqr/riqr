# Generated by Django 3.2.8 on 2021-12-15 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_register_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nationalities',
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
    ]
