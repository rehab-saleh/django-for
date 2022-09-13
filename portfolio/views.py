from django.shortcuts import render
from .models import *

# Create your views here.


def portfolio(request):
    info = Informations.objects.get(name="Rehab saleh Gomaa")
    projects = Projects.objects.all()
    context = {'info': info, 'projects':projects}

    return render(request, 'portfolio/about.html', context)

#def home(request):
    #return render(request, 'portfolio/home.html')
