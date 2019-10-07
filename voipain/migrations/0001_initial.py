# Generated by Django 2.2.5 on 2019-10-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=1)),
            ],
        ),
    ]
