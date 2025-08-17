from celery import shared_task
from django.core.mail import send_mail
from .models import Payment

@shared_task
def send_payment_confirmation_email(payment_id):
    payment = Payment.objects.get(id=payment_id)
    subject = "Booking Payment Confirmation"
    message = f"Your booking {payment.booking.id} has been paid successfully."
    recipient = [payment.booking.user.email]
    send_mail(subject, message, "noreply@travelapp.com", recipient)
