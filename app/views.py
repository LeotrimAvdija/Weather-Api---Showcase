from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
import urllib.request
import json

def index(request):

    search = request.POST.get('search')
    search_url = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={search}&appid=cb771e45ac79a4e8e2205c0ce66ff633").read()
    convert = json.loads(search_url)


    #data api
    temp = convert['main']['temp']
    feels_like = convert['main']['feels_like']
    max_temp = convert['main']['temp_max']
    min_temp = convert['main']['temp_min']
    humidity = convert['main']['humidity']
    clouds = convert['clouds']['all']
    main_description = convert['weather'][0]['main']
    description = convert['weather'][0]['description']
    pressure = convert['main']['pressure']
    speed = convert['wind']['speed']
    sys = convert['sys']['country']
    lat = convert['coord']['lat']
    lon = convert['coord']['lon']

    Final = f'{main_description} : {description}'



    #Data manipulation
    #Temperature
    temp = str(temp -273)
    temp = temp [:4]

    #Fells like
    feels_like = str(feels_like -273)
    feels_like = feels_like [:4]
    

    #Temp Max
    max_temp = str(max_temp -273)
    max_temp = max_temp [:4]


    #Temp Min
    min_temp = str(min_temp -273)
    min_temp = min_temp [:4]

    #Pressure Bar
    pressure = pressure / 1000



    context = {
        'temp':temp,
        'feels_like':feels_like,
        'max_temp':max_temp,
        'min_temp':min_temp,
        'humidity':humidity,
        'clouds':clouds,
        'description':description,
        'Final':Final,
        'pressure':pressure,
        'speed':speed,
        'sys':sys,
        'lat':lat,
        'lon':lon,
    }




    return render(request, 'index.html',context)