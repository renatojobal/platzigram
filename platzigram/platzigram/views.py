"""Platzi views.py"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))


def hi(request):
    return HttpResponse('Hi!')

def order_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers.sort()
    data = {
        'status': 'ok',
        'numbers': numbers,
        'msg': 'Exiticing'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')