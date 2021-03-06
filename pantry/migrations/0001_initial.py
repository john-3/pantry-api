# Generated by Django 3.0.1 on 2020-08-26 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Group')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Storage')),
            ],
        ),
    ]
