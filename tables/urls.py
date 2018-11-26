from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('piechart', views.piechart, name='piechart'),
    path('charts', views.charts, name='charts')
]