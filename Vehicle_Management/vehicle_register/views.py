from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from .models import *



# Create your views here.

def index(request):
    return render(request, 'index.html')



