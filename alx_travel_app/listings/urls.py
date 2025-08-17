"""
listings/urls.py
----------------
Routes for the listings app – included from project‑level urls.py.
"""


from django.urls import path, include
from .views import ListingListCreateView, ListingViewSet,BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # /api/listings/
    path('api/', include(router.urls)),

    path("listings/", ListingListCreateView.as_view(), name="listing-list-create")
]





