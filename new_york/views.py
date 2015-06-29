from django.shortcuts import render
from django.http import HttpResponse
import json, os

# Create your views here.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
	
	json_data = open(os.path.join(base_dir, 'static/data.json')).read()
	json_dict = json.loads(json_data)
	
	return HttpResponse("Hello world!")
