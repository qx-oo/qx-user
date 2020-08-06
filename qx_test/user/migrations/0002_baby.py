# Generated by Django 3.0.8 on 2020-08-06 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('type', models.CharField(db_index=True, max_length=10, verbose_name='类型')),
                ('object_id', models.PositiveIntegerField(db_index=True, verbose_name='对象Id')),
                ('name', models.CharField(default='', max_length=50, verbose_name='名称')),
            ],
            options={
                'verbose_name': 'Baby',
                'verbose_name_plural': 'Baby',
            },
        ),
    ]
