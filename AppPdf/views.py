from django.shortcuts import render
from .models import *


# Create your views here.
def accept(request):
    return render(request, 'accept.html')
