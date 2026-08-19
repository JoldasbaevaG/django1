from django.urls import path
from .views import blog, news, faq, portfolio, profile

urlpatterns = [
    path('blog/', blog),
    path('news/', news),
    path('faq/', faq),
    path('portfolio/', portfolio),
    path('profile/', profile),

]
