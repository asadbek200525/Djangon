# Generated by Django 4.0.3 on 2022-03-26 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('fam', models.CharField(max_length=40)),
                ('yosh', models.IntegerField()),
                ('brithday', models.DateTimeField()),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.fanlar')),
            ],
        ),
    ]
