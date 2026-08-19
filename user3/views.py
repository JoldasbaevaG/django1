from django.http import HttpResponse

def settings(request):
    return HttpResponse("Sozlamalar sahifasi")


def terms(request):
    return HttpResponse("Foydalanish shartlari")


def privacy(request):
    return HttpResponse("Maxfiylik siyosati")


def search(request):
    return HttpResponse("Qidiruv natijalari")


def page_not_found(request):
    return HttpResponse("Sahifa topilmadi (404)")