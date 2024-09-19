from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests

def weather_home(request):
    return render(request, 'weather.html')

def get_weather(request):
    if request.method == 'POST':
        api_key = '9bea4413a3c8cd354b91aa1e9998b60a'
        city = request.POST.get('country', '')

        if city:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
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
                return render(request, 'weather_info.html', {'weather_data': weather_data})
            else:
                # Handle the case where the city is not found or another error occurs
                return render(request, 'weather.html', {'error': 'City not found or other error occurred.'})
        else:
            # Handle the case where no city is provided
            return render(request, 'weather.html', {'error': 'No city provided.'})

    return redirect('home')  # Redirect to home if no data

def download_weather(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'No city specified'}, status=400)

    api_key = '9bea4413a3c8cd354b91aa1e9998b60a'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(weather_url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to retrieve weather data'}, status=response.status_code)

    weather_data = response.json()

    csv_content = f"City,Weather,Temperature,Humidity\n"
    csv_content += f"{city},{weather_data['weather'][0]['description']},{weather_data['main']['temp']},{weather_data['main']['humidity']}\n"

    response = HttpResponse(csv_content, content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{city}_weather.csv"'

    return response
