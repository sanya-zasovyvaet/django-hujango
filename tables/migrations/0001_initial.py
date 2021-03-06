# Generated by Django 2.1.2 on 2018-10-11 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Carriage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carriage_code', models.CharField(max_length=4)),
                ('carriage_capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=50)),
                ('travel_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField(default=0)),
                ('carriage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Carriage')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=50)),
                ('station_address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.City')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_position', models.IntegerField()),
                ('arrival_time', models.DateTimeField(verbose_name='arrival time')),
                ('deport_time', models.DateTimeField(verbose_name='deport time')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Route')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_name', models.CharField(max_length=20)),
                ('discount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deport_date', models.DateTimeField(verbose_name='deport time')),
                ('ticket_cost', models.FloatField(default=0.0)),
                ('payed_with_card', models.BooleanField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Route')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Seat')),
                ('station_arrive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_arrive', to='tables.Stop')),
                ('station_deport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_deport', to='tables.Stop')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=50)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Route')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('user_fullname', models.CharField(max_length=50)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Card')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role_name', models.CharField(max_length=50)),
                ('access_level', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.UserRole'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.User'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Country'),
        ),
        migrations.AddField(
            model_name='carriage',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Train'),
        ),
        migrations.AddField(
            model_name='card',
            name='tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Tariff'),
        ),
    ]
