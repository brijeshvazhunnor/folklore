from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('payment/<int:registration_id>/', views.payment, name='payment'),
]
