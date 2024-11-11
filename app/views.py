from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    EMTFO=TopicmodelForm()
    d={'EMTFO':EMTFO}
    if request.method=='POST':
        ABCD=TopicmodelForm(request.POST)
        if ABCD.is_valid():
            ABCD.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EMWFO=WebpagemodelForm()
    d={'EMWFO':EMWFO}
    if request.method=='POST':
        EFGH=WebpagemodelForm(request.POST)
        if EFGH.is_valid():
            EFGH.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_webpage.html',d)


def wish(request,name):
    return HttpResponse(f'{name} is a framework')