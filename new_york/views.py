from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json, os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
	
	json_open = open(os.path.join(base_dir, 'static/data.json')).read()
	json_dict = json.loads(json_open)

	def filter():
		saved = []
		for a in json_dict["data"]:
			saved = saved + [a[8:]]
		return saved

	filtered = filter()
	return render(request, 'index.html', {'json':json_dict, 'filtered':paginate(request, filtered)})

def paginate(request, to_paginate):
    paginator = Paginator(to_paginate, 10)

    page = request.GET.get('page')
    try:
        paginated = paginator.page(page)
    except PageNotAnInteger:
        paginated = paginator.page(1)
    except EmptyPage:
        paginated = paginator.page(paginator.num_pages)

    return paginated