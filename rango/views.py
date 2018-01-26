# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #A dictionary providing context for the template engine
    context_dict = {'boldmessage' : "Stand and deliver, your money or your life!"}

    #Return a rendered response to the client
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return render(request, 'rango/about.html')

