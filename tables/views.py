from django.shortcuts import render
from django.http import HttpResponse

import matplotlib
import io
import matplotlib.pyplot as plt

from .models import Card, Tariff

def index(request):
    return HttpResponse("eeeeeee rabotaet")

def piechart(request):
    tariffs = Tariff.objects.all().values()
    cards = Card.objects.all().values()

    data = []
    labels = []

    for t in tariffs:
        data.append(len(cards.filter(tariff_id=t['id'])))
        labels.append(t['tariff_name'])

    f = matplotlib.figure.Figure()
    buf = io.BytesIO()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(f)

    ax1 = f.add_subplot(111)
    ax1.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    # if required clear the figure for reuse 
    f.clear()
    response['Content-Length'] = str(len(response.content))

    return response

def charts(request):
    tariffs = Tariff.objects.all().values()
    cards = Card.objects.all().values()
    cards_dict = {}

    for t in tariffs:
        cards_dict[t['tariff_name']] = len(cards.filter(tariff_id = t['id']))

    context = {'cards_dict': cards_dict}
    return render(request, 'tables/charts.html', context)