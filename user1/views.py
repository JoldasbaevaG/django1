from django.http import HttpResponse

def r(request):
    return HttpResponse("Hello Django")
