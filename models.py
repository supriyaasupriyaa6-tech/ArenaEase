from django.db import models

class ArenaBooking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    stadium = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    slot = models.CharField(max_length=50)
    
    # NEW: Price field for revenue tracking
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    
    # STATUS: Tracks if they paid or just reserved
    STATUS_CHOICES = [
        ('Reserved', 'Reserved (Unpaid)'),
        ('Booked', 'Booked (Paid)'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Reserved')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.stadium} ({self.status})"