from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('hello world') #alt enter를 통해 import를 해줄수 있음