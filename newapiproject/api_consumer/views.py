from django.shortcuts import render

import requests
from django.http import JsonResponse

API_URL = "http://127.0.0.1:8000/api/items/"

def get_items(request):
    # Make a GET request to the existing API
    response = requests.get(API_URL)
    
    # If the request is successful, return the response data
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Unable to fetch items'}, status=500)
