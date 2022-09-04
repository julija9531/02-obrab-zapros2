from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open("data-398-2018-08-30.csv", encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        reader = list(rows)

    DATA_Bus_Stop = []
    for busstop in reader:
        DATA_Bus_Stop.append({'Name': busstop[1], 'Street': busstop[4], 'District': busstop[6]})
    DATA_Bus_Stop.pop(0)

    paginator = Paginator(DATA_Bus_Stop, 10)
    page_num = int(request.GET.get('page', 1))
    page = paginator.get_page(page_num)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
