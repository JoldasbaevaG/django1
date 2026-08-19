from django.urls import path
from .views import gallery, pricing, team, reviews, support

urlpatterns = [
    path('gallery/', gallery),
    path('pricing/', pricing),
    path('team/', team),
    path('reviews/', reviews),
    path('support/', support),
]
