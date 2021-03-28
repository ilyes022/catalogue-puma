from django.shortcuts import render
from django.http import HttpResponse



def catalogue (request) :

    return render(request, "catalogue.html")