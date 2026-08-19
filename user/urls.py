from django.urls import path
from .views import u, home, about, contact, services

urlpatterns = [
    path('gumisay/', u),
    path('a', home),
    path('about/', about),
    path('contact/', contact),
    path('services/', services),

]
