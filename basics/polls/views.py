from django.shortcuts import render
from django.http import HttpResponse

def kate(request):
    body = """
    <doctype html>
    <html lang="en">
    <head>
    </head>
    <body>
    <h1>This is kate.</h1>
    </body>
    </html>
    """
    return HttpResponse(body)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bob(request):
    return HttpResponse("This is bob.")