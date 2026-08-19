from django.urls import path
from .views import courses, cart, checkout, partners, career

urlpatterns = [
    path('courses/', courses),
    path('cart/', cart),
    path('checkout/', checkout),
    path('partners/', partners),
    path('career/', career),
]
