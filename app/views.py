import json
from django.http import HttpResponse
from django.http import JsonResponse

def qush(requets):
    body = requets.body.decode()
    dict = json.loads(body)
    return JsonResponse({'a+b':dict['a']+dict['b']})

def ayir(requets):
    body = requets.body.decode()
    dict = json.loads(body)
    return JsonResponse({'a-b':dict['a']-dict['b']})

def kupaytir(requets):
    body = requets.body.decode()
    dict = json.loads(body)
    return JsonResponse({'a*b':dict['a']*dict['b']})

def bul(requets):
    body = requets.body.decode()
    dict = json.loads(body)
    return JsonResponse({'a:b':dict['a']/dict['b']})
