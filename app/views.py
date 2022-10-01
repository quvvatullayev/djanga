import json
from django.http import HttpResponse
from django.http import JsonResponse

def sum_num(requets):
    a = requets.body.decode()
    dict = json.loads(a)
    r = JsonResponse({'sum':dict['a'] + dict['b']})
    return r
