from django.http import HttpResponse


def u(request):
    return HttpResponse("Hi Django")