from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    sum = int(a) + int(b)
    r = JsonResponse({'sum':sum})

    return r

urlpatterns = [
    path('', home),
]
