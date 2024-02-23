from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handaler
# action


def say_hello(request):
    # pull Data from database
    # Transform Data
    # Send Email
    return HttpResponse("Hello World")


def say_hello_html(request):
    return render(request, "index.html", {"name": "Black"})
