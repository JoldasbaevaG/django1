from django.http import HttpResponse

def gallery(request):
    return HttpResponse("Rasmlar galereyasi")


def pricing(request):
    return HttpResponse("Narxlar va tariflar")


def team(request):
    return HttpResponse("Bizning jamoa")


def reviews(request):
    return HttpResponse("Mijozlar fikrlari")


def support(request):
    return HttpResponse("Qo'llab-quvvatlash xizmati")
