from django.http import HttpResponse, JsonResponse
from .models import Person


def html(request):
    return HttpResponse(f"<html><head></head><body>{Person.objects.first()}</body></html>")


def ajax(request):
    Person.objects.first()
    return JsonResponse({'sss': 1})
