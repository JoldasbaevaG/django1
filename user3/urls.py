from django.urls import path
from .views import settings, terms, privacy, search, page_not_found

urlpatterns = [
    path('settings/', settings),
    path('terms/', terms),
    path('privacy/', privacy),
    path('search/', search),
    path('404/', page_not_found),
]