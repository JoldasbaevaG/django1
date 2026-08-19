from django.http import HttpResponse

def courses(request):
    return HttpResponse("O'quv kurslari")


def cart(request):
    return HttpResponse("Savat sahifasi")


def checkout(request):
    return HttpResponse("To'lovni rasmiylashtirish")


def partners(request):
    return HttpResponse("Hamkorlarimiz")


def career(request):
    return HttpResponse("Bo'sh ish o'rinlari")