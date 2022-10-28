from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=2d10e43f69b199b2fade9f3bfe1ad387').read()

        listOfData = json.loads(source)

        data = {
            "countryCode" : str(listOfData['sys']['country']),
            "coordinate" : 
            "temp"
            "pressure"
            "humidity"
            "main"
            "description"
            "icon"
        }
