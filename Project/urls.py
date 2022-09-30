from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    if b == None:
        b = 0
    if a == None:
        a = 0
    sum = int(a) + int(b)
    r = JsonResponse({'sum':sum})

    return r

urlpatterns = [
    path('', home),
]
