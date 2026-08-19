from django.http import HttpResponse

def r(request):
    return HttpResponse("Hello Django")
    
def blog(request):
    return HttpResponse("Blog sahifasi")


def news(request):
    return HttpResponse("Yangiliklar")


def faq(request):
    return HttpResponse("Ko'p beriladigan savollar")


def portfolio(request):

    return HttpResponse("Loyiha va ishlar")


def profile(request):
    return HttpResponse("Foydalanuvchi profili")