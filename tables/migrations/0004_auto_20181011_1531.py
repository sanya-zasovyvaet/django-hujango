# Generated by Django 2.1.2 on 2018-10-11 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20181011_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Card'),
        ),
    ]
