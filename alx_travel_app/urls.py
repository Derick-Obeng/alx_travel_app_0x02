# urls.py (excerpt)

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from alx_travel_app.listings import urls

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version="v1",
        description="API documentation for ALX Travel App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('alx_travel_app.listings.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("api/", include("alx_travel_app.listings.urls")),
]
