# Generated by Django 2.0.4 on 2018-04-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20180411_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('blogpost', models.TextField()),
            ],
        ),
    ]
