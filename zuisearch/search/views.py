from django.shortcuts import render
from django.http import Http404
from search.models import *
from django.views.decorators.csrf import csrf_exempt
import math
# Create your views here.
def index(request):
    return render(request, 'index.html', locals())
def home(request):
    try:
        site_list = Home.objects.filter(position=False)
        school_site = Home.objects.filter(position=True)
    except Home.DoseNotExist:
        raise Http404
    return render(request, 'home.html', locals())
def nav(request):
    try:
        column = Column.objects.all()
        right_data =[]
        li_data = []
        for co in column:
            right_item = Site.objects.filter(column=co)
            count = math.ceil(len(right_item)/16)
            count_li = []
            for i in range(1, count):
                count_li.append(i)
            right_data.append(right_item)
            li_data.append(count_li)
    except Column.DoseNotExist:
        raise Http404            
    return render(request, 'nav.html', locals())
def detail(request,id):
    try:
        site = Site.objects.get(id=str(id))
    except Site.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', locals())