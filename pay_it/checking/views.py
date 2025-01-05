from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def checking(request):
    template = loader.get_template('log.html')
    return HttpResponse(template.render())

