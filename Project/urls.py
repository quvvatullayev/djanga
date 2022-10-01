from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse
from app.views import sum_num

urlpatterns = [
    path('', sum_num)
]
