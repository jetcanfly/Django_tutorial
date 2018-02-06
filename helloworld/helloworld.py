__author__ = 'jet'
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Django.")


