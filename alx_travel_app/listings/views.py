"""
listings/views.py
-----------------
Request handlers for the /api/listings/ endpoint.

We start with DRF’s generic class‑based views so we get CRUD quickly.
"""
import uuid
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets



class ListingListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/listings/   -> list all listings
    POST /api/listings/   -> create a new listing
    """
    queryset = Listing.objects.all().order_by("-created_at")  # newest first
    serializer_class = ListingSerializer



class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class InitiatePaymentView(View):
    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            tx_ref = str(uuid.uuid4())
            payment = Payment.objects.create(
                booking=booking,
                amount=booking.total_price,
                chapa_tx_ref=tx_ref,
                status="PENDING"
            )

            url = "https://api.chapa.co/v1/transaction/initialize"
            headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
            data = {
                "amount": str(booking.total_price),
                "currency": "ETB",
                "email": booking.user.email,
                "tx_ref": tx_ref,
                "callback_url": "http://localhost:8000/api/verify-payment/",
                "return_url": "http://localhost:8000/success/"
            }

            response = requests.post(url, headers=headers, data=data)
            res_data = response.json()

            if res_data.get("status") == "success":
                checkout_url = res_data["data"]["checkout_url"]
                return JsonResponse({"checkout_url": checkout_url}, status=200)
            else:
                payment.status = "FAILED"
                payment.save()
                return JsonResponse({"error": "Payment initiation failed"}, status=400)

        except Booking.DoesNotExist:
            return JsonResponse({"error": "Booking not found"}, status=404)
        

class VerifyPaymentView(View):
    def get(self, request, tx_ref):
        url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}

        response = requests.get(url, headers=headers)
        res_data = response.json()

        try:
            payment = Payment.objects.get(chapa_tx_ref=tx_ref)
            if res_data.get("status") == "success" and res_data["data"]["status"] == "success":
                payment.status = "COMPLETED"
                payment.save()
                # trigger Celery task to send email here
                return JsonResponse({"message": "Payment successful"}, status=200)
            else:
                payment.status = "FAILED"
                payment.save()
                return JsonResponse({"message": "Payment failed"}, status=400)
        except Payment.DoesNotExist:
            return JsonResponse({"error": "Payment not found"}, status=404)
        

        # Trigger Celery task to send email
        from .tasks import send_payment_confirmation_email
        send_payment_confirmation_email.delay(payment.id)
        