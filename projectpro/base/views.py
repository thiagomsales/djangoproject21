


# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Project Pro 21<body><html>', content_type='text/html')
