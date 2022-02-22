# Generated by Django 3.2.8 on 2021-11-23 14:12

import pages.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('file', models.FileField(upload_to=pages.models.upload_path_handler)),
            ],
        ),
        migrations.CreateModel(
            name='Nationalities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('otchestvo', models.CharField(blank=True, max_length=25, verbose_name='Отчество')),
                ('place_of_birth', models.CharField(blank=True, max_length=30, verbose_name='Место рождения')),
                ('place_of_death', models.CharField(blank=True, max_length=30, verbose_name='Место смерти')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Дата смерти')),
                ('avatar', models.CharField(blank=True, max_length=70, null=True)),
                ('videos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=70), blank=True, default=list, size=None)),
                ('pictures', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=70), blank=True, default=list, size=None)),
                ('biography', models.TextField(blank=True, max_length=2000, verbose_name='Биография')),
                ('date_of_creation', models.DateField(null=True, verbose_name='Дата создания')),
                ('payed', models.BooleanField(default=False, verbose_name='Оплата')),
                ('price', models.IntegerField(default=1390, verbose_name='Цена')),
                ('private', models.BooleanField(default=False, verbose_name='Скрыта')),
                ('facts', models.CharField(blank=True, max_length=200, null=True, verbose_name='Факты')),
                ('nationality', models.IntegerField(blank=True, default=165, verbose_name='Национальность')),
                ('coords', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('hash', models.CharField(blank=True, max_length=50, verbose_name='Хэш')),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=6)),
                ('verified', models.BooleanField(default=False)),
                ('telephone_number', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('array_of_pages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10, null=True), default=list, null=True, size=None)),
                ('vk', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('access_vk', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]