# Generated by Django 2.1.2 on 2018-10-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('operand1', models.CharField(max_length=15)),
                ('operator', models.CharField(max_length=1)),
                ('operand2', models.CharField(max_length=15)),
            ],
        ),
    ]
