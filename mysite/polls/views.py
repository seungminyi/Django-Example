from django.http import HttpRequest


def index(request):
    return HttpRequest("Hello, world. You're at the polls index.")
# Create your views here.
