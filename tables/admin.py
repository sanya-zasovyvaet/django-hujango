from django.contrib import admin

from .models import Country, City, Station, Stop, Route, Train, Carriage, Seat, Tariff, Card, UserRole, User, Ticket

class CarriagesInLine(admin.TabularInline):
    model = Carriage
    extra = 3

class StopsInLine(admin.StackedInline):
    model = Stop
    extra = 3

class CitiesInLine(admin.TabularInline):
    model = City
    extra = 3

class RouteAdmin(admin.ModelAdmin):
    inlines = [StopsInLine]
    list_display = ('route_name', 'travel_time')
    search_fields = ('route_name',)

class TrainAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['train_name']}),
        ('Route', {'fields': ['route']}),
    ]
    inlines = [CarriagesInLine]
    list_display = ('train_name', 'route')
    search_fields = ('train_name',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_code')
    search_fields = ('country_name', 'country_code')
    inlines = [CitiesInLine]

class CarriageAdmin(admin.ModelAdmin):
    list_display = ('carriage_code', 'train')
    search_fields = ('carriage_code',)

class StopAdmin(admin.ModelAdmin):
    list_display = ('station', 'route', 'route_position', 'arrival_time', 'deport_time')
    list_filter = ['station']

class TicketAdmin(admin.ModelAdmin):
    list_display = ('route', 'user', 'deport_date', 'station_deport', 'station_arrive', 'seat', 'ticket_cost', 'payed_with_card')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'carriage')
    search_fields = ('seat_number',)
    list_filter = ['carriage']

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country')
    search_fields = ('city_name',)
    list_filter = ['country']

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'city', 'station_address')
    search_fields = ('station_name',)
    list_filter = ['city']

class TariffAdmin(admin.ModelAdmin):
    list_display = ('tariff_name', 'discount')
    list_filter = ['tariff_name']

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_role_name', 'access_level')
    search_fields = ('user_role_name',)
    list_filter = ['access_level']

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_fullname', 'card', 'role')
    search_fields = ('username', 'user_fullname')

admin.site.register(Country, CountryAdmin) 
admin.site.register(City, CityAdmin) 
admin.site.register(Station, StationAdmin) 
admin.site.register(Stop, StopAdmin) 
admin.site.register(Route, RouteAdmin) 
admin.site.register(Train, TrainAdmin) 
admin.site.register(Carriage, CarriageAdmin) 
admin.site.register(Seat, SeatAdmin) 
admin.site.register(Tariff, TariffAdmin) 
admin.site.register(Card) 
admin.site.register(UserRole, UserRoleAdmin) 
admin.site.register(User, UserAdmin)
admin.site.register(Ticket, TicketAdmin)