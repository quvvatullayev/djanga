import json
from django.http import HttpResponse
from django.http import JsonResponse

def sum_num(requets):
    a = requets.body.decode()
    dict = json.loads(a)
    r = JsonResponse({'sum':dict['a'] + dict['b']})
    return r

def sum_num(requets):
    a = requets.body.decode()
    dict = json.loads(a)
    r = JsonResponse({'sum':dict['a'] + dict['b']})
    return r

def helov(requets):
    return HttpResponse('<h1>Hellov</h1>')

def Hom(requets):
    return HttpResponse('<h1>Hom</h1>')

def abaut(requets):
    return HttpResponse('<h1>Abaut</h1>')

def uy(requets):
    return HttpResponse('<h1>Uy</h1>')
