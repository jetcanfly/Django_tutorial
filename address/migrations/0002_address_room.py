# Generated by Django 2.0.1 on 2018-02-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='room',
            field=models.CharField(default='', max_length=10, verbose_name='房间'),
        ),
    ]