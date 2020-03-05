from django.shortcuts import render
from django.http import HttpResponse

def kate(request):
    return HttpResponse("This is kate.")

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bob(request):
    return HttpResponse("This is bob.")