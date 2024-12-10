from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<h1><i>Hello!!! this is a testing to work with docker .......</i>😎🤘</h1>')