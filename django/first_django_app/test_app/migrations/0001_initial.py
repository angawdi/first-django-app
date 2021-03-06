# Generated by Django 2.1.1 on 2018-09-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('award_winning', models.BooleanField(default=False)),
            ],
        ),
    ]
