# Generated by Django 2.0.4 on 2018-04-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogpost',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
