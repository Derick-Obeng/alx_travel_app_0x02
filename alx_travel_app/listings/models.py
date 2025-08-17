"""
listings/models.py
------------------
Defines database tables for the *listings* app.

One Listing == one travel experience / package.
"""

from django.db import models
from django.conf import settings


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.guest_name} booking for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Review by {self.reviewer_name} for {self.listing.title}"



class Payment(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    booking = models.ForeignKey("Booking", on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    chapa_tx_ref = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.id} - {self.status}"
