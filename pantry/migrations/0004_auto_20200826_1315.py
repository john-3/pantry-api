# Generated by Django 3.0.1 on 2020-08-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0003_auto_20200826_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(choices=[('Dairy', 'Dairy'), ('Meat', 'Meat'), ('FV', 'FV'), ('Grain', 'Grain')], default='Dairy', max_length=10),
        ),
        migrations.AlterField(
            model_name='storage',
            name='name',
            field=models.CharField(choices=[('Refrigerator', 'Refrigerator'), ('Freezer', 'Freezer'), ('Pantry', 'Pantry')], default='Refrigerator', max_length=12),
        ),
    ]