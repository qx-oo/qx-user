# Generated by Django 3.0.8 on 2020-08-02 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('account', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='账号')),
                ('mobile', models.CharField(blank=True, db_index=True, max_length=25, null=True, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('last_access_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最近访问时间')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'swappable': 'AUTH_USER_MODEL',
                'unique_together': {('mobile', 'email')},
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('name', models.CharField(default='', max_length=50, verbose_name='用户名称')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UserInfo',
            },
        ),
    ]
