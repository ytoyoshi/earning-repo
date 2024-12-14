from django.shortcuts import render
from django.http import HttpResponse

def helloWorldappview(request):
    return HttpResponse('APP called!!!')
