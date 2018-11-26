from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2)
    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name

class Tariff(models.Model):
    tariff_name = models.CharField(max_length=20)
    discount = models.FloatField(default=0.0)
    def __str__(self):
        return self.tariff_name

class Station(models.Model):
    station_name = models.CharField(max_length=50)
    station_address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.station_name

class Route(models.Model):
    route_name = models.CharField(max_length=50)
    travel_time = models.IntegerField(default=0)
    def __str__(self):
        return self.route_name

class Train(models.Model):
    train_name = models.CharField(max_length=50)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    def __str__(self):
        return self.train_name

class Carriage(models.Model):
    carriage_code = models.CharField(max_length=4)
    carriage_capacity = models.IntegerField(default=0)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    def __str__(self):
        return self.carriage_code

class Seat(models.Model):
    seat_number = models.IntegerField(default=0)
    carriage = models.ForeignKey(Carriage, on_delete=models.CASCADE)

class Card(models.Model):
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    def __str__(self):
        return self.tariff.__str__()

class UserRole(models.Model):
    user_role_name = models.CharField(max_length=50)
    access_level = models.IntegerField(default=0)
    def __str__(self):
        return self.user_role_name

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    user_fullname = models.CharField(max_length=50)
    card = models.ForeignKey(Card, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Stop(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_position = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField('arrival time')
    deport_time = models.DateTimeField('deport time')
    def __str__(self):
        return self.station.__str__()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    deport_date = models.DateTimeField('deport time')
    ticket_cost = models.FloatField(default=0.0)
    station_deport = models.ForeignKey(Stop, related_name='station_deport', on_delete=models.CASCADE)
    station_arrive = models.ForeignKey(Stop, related_name='station_arrive', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    payed_with_card = models.BooleanField()
