from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Registration
from .forms import RegistrationForm




def home(request):
    return render(request, 'home.html')

def brochures(request):
    return render(request, 'brochures.html')

