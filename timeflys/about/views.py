from django.shortcuts import render
from django.http import HttpResponse
from .models import People


def index(request):
    about_us = People.objects.order_by('Name')
    context = {'about_us': about_us}
    return render(request, 'about.html', context)
    # return render(request, 'about.html')

  