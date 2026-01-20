from django.http import JsonResponse
from django.views import View
from weather.utils import fetch_weather_data

class WeatherDetailView(View):
    """
    View to handle requests for weather details of a specific city
    """
    
    def get(self,request):
        city = request.GET.get('city')
        aqi = request.GET.get('aqi','no')

        # get city from json request
        city2 = request.GET.get('city')

        if not city:
            return JsonResponse({"error":"City parameter is required"}, status= 400)
        
        # call utils function to fetch weather  data
        data, error = fetch_weather_data(city, aqi)

        if error:
            return JsonResponse(data, status=error)
        return JsonResponse(data, status=200)
