from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Registration
from .forms import RegistrationForm




def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.payment_status = False  # set false until paid
            instance.save()

            # Redirect to payment with ID
            return redirect('payment', registration_id=instance.id)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def payment(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'payment.html', {'registration': registration})
