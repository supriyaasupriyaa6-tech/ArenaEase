from django.contrib import admin
from django.urls import path, include
# This import is the "bridge" to your app's functions
from djangoapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # These paths use the 'views' we just imported
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('stadiums/', views.stadium_details, name='stadiums'),
    path('availability/', views.availability, name='availability'),
    path('booking/', views.booking, name='booking'),
    path('process-booking/', views.process_booking, name='process_booking'),
    path('booking-confirmed/', views.booking_confirmed, name='booking_confirmed'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('facilities/', views.facilities, name='facilities'),
    path('policy/', views.policy, name='policy'),
    path('gallery/', views.gallery, name='gallery'),
]