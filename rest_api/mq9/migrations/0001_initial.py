# Generated by Django 4.2.7 on 2023-11-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MQ9',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('co', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'MQ9',
                'verbose_name_plural': 'MQ9',
                'ordering': ['-time'],
            },
        ),
    ]
