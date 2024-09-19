from django.shortcuts import render
import requests

def weather_view(request):
    api_key = '9bea4413a3c8cd354b91aa1e9998b60a'
    weather_data = None

    if request.method == 'POST':
        country = request.POST.get('country')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        else:
            weather_data = {
                'location': 'N/A',
                'temperature': 'N/A',
                'condition': 'N/A',
                'humidity': 'N/A',
                'wind_speed': 'N/A'
            }

    return render(request, 'weather.html', {'weather_data': weather_data})