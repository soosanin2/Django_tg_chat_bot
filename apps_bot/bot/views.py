from django.shortcuts import render


from django.http import HttpResponse

def start(request):
    return HttpResponse("Hello, this is the start view!")