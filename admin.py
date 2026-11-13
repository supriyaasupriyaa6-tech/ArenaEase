from django.contrib import admin
from django.db.models import Sum
from .models import ArenaBooking

@admin.register(ArenaBooking)
class ArenaBookingAdmin(admin.ModelAdmin):
    # Columns to show in the list
    list_display = ('full_name', 'stadium', 'price', 'status', 'created_at')
    
    # Filters and Search bar
    list_filter = ('status', 'stadium')
    search_fields = ('full_name', 'email', 'stadium')
    
    # Bulk action to mark as Paid
    actions = ['make_booked']

    @admin.action(description='Mark selected bookings as PAID (Booked)')
    def make_booked(self, request, queryset):
        queryset.update(status='Booked')
        self.message_user(request, "Selected slots have been updated to PAID.")

    # Logic to show Total Revenue at the top
    def changelist_view(self, request, extra_context=None):
        # Calculate sum of all 'Booked' entries
        total_rev = ArenaBooking.objects.filter(status='Booked').aggregate(Sum('price'))['price__sum'] or 0
        
        # Display as a banner message
        self.message_user(request, f"💰 Total Revenue (Paid): ₹{total_rev}", level='info')
        
        return super().changelist_view(request, extra_context=extra_context)