from django.shortcuts import render
from django.http import HttpResponse
# Request Handler

def hello_world(request):
    return render(request,'hello.html')