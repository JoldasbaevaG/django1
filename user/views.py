from django.http import HttpResponse


def u(request):
    return HttpResponse("Hi Django")

def home(request):
    return HttpResponse("Bas menu")


def about(request):
    return HttpResponse("Biz haqimizda")


def contact(request):
    return HttpResponse("Aloqa sahifasi")


def services(request):
    return HttpResponse("Xizmatlar sahifasi")