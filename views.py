from django.shortcuts import render, redirect
from .models import ArenaBooking

# --- PAGE RENDERING FUNCTIONS ---

def index(request):
    return render(request, 'djangoapp/AE_index.html')

def about(request):
    return render(request, 'djangoapp/AE_about.html')

def stadium_details(request):
    return render(request, 'djangoapp/AE_stadium_details.html')

def availability(request):
    return render(request, 'djangoapp/AE_availability.html')

def booking(request):
    return render(request, 'djangoapp/AE_booking.html')

# Keep this to prevent the URL error
def booking_confirmed(request):
    return render(request, 'djangoapp/AE_booking_confirmed.html')

def payment(request):
    return render(request, 'djangoapp/AE_payment.html')

def contact(request):
    return render(request, 'djangoapp/AE_contact.html')

def facilities(request):
    return render(request, 'djangoapp/AE_facilities.html')

def policy(request):
    return render(request, 'djangoapp/AE_policy.html')

def gallery(request):
    return render(request, 'djangoapp/AE_gallery.html')

# --- DATABASE LOGIC ---

def process_booking(request):
    if request.method == "POST":
        new_entry = ArenaBooking(
            full_name=request.POST.get('userName'),
            email=request.POST.get('userEmail'),
            stadium=request.POST.get('stadiumName'),
            sport=request.POST.get('sportName'),
            slot=request.POST.get('slotTime'),
            price=500.00,  # Default price from your model
            status='Reserved' # Match your STATUS_CHOICES
        )
        new_entry.save()
        return render(request, 'djangoapp/AE_booking.html', {'booking': new_entry})
    
    return redirect('availability')