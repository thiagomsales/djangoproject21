


# Create your views here.
from django.http import HttpResponse


def home(request):
    raise ValueError()
    return HttpResponse('<html><body>Project Pro 21<body><html>', content_type='text/html')
