from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import House
from django.core.paginator import Paginator
import pickle
# Create your views here.
import numpy as np
import json
import os


Locations = None
Data_columns = None
Model = None


def get_price(location, sqft, bhk, bath):
    try:
        loc_index = Data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(Data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(Model.predict([x])[0], 2)


def load():
    global Data_columns
    global Locations

    with open("static/columns.json", "r") as f:
        Data_columns = json.load(f)['data_columns']
        Locations = Data_columns[3:]

    global Model
    if Model is None:
        with open('./model/model.pickle', 'rb') as f:
            Model = pickle.load(f)


def get_location_names():
    return Locations


def get_data_columns():
    return Data_columns


def home(request):
    load()
    house = House.objects.all().order_by('-post_creatDate')[0:4]
    context = {
        'house': house,
        'location': Locations
    }
    return render(request, 'home.html', context)


def contactUs(request):
    return render(request, 'contactUs.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def houses(request):
    Post = House.objects.all().order_by('-post_creatDate')
    paginator = Paginator(Post, 4)
    page = request.GET.get('page')
    context = {
        'Posts': Post
    }
    return render(request, 'houses.html', context)


def readMore(request, slug):
    house = House.objects.filter(houseId=slug).first()
    context = {
        'house': house,
    }
    return render(request, 'readMore.html', context)


def showPrice(request):
    if request.method == 'POST':
        area = request.POST['Area']
        bhk = request.POST['BHK']
        bathrooms = request.POST['Bathrooms']
        location = request.POST['Location']
        load()
        pre_price = get_price(location, area, bhk, bathrooms)
        context = {
            'area': area,
            'bhk': bhk,
            'bathrooms':bathrooms,
            'location':location,
            'pre_price':pre_price
        }
        return render(request, 'showPrice.html', context)
