from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json, os

# Create your views here.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
	
	json_open = open(os.path.join(base_dir, 'static/data.json')).read()
	json_data = JsonResponse(json_open, safe=False)
	return render(request, 'index.html')
