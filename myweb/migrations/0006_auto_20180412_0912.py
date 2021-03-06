# Generated by Django 2.0.4 on 2018-04-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0005_auto_20180411_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='answer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='question',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
