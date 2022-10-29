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
            "coordinate" : str(listOfData['coord']['lat']) + ", " + str(listOfData['coord']['lon']),
            "temp" : str(listOfData['main']['temp'] - 273),
            "pressure" : str(listOfData['main']['pressure']),
            "humidity" : str(listOfData['main']['humidity']),
            "main" : str(listOfData['weather'][0]['main']),
            "description" : str(listOfData['weather'][0]['description']),
            "icon" : str(listOfData['weather'][0]['icon'])
        }
