# Generated by Django 2.0.1 on 2018-02-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagename', models.CharField(max_length=20, unique=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
