"""Vista de RED"""
# DJANGO
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting(Saludo)."""
      
    return HttpResponse('Wena nico tu hora es {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
         content_type='application/json'
         )

def say_hi(request, name, age):
    """Returtn a greeting"""
    if age <12:
        message = 'Sorry {}, you are not allowed here'. format(name)
    else:
        message= 'Hello, {}! Welcome to RED'. format(name)
    return HttpResponse(message)
    