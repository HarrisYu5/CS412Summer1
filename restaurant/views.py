from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpRequest
import random

# Create your views here.

daily_specials = [
    'stir fried manchorian scorpian',
    'sea cucumber flavored ice cream',
    'deep fried tarantula',
    'sautéed rattlesnake',
]
    
def main(request):
    template = 'restaurant/main.html'
    return render(request, template)

def order(request):
    template = 'restaurant/order.html'
    context = {
        'daily_special': random.choice(daily_specials) 
    }
    return render(request, template, context)

def confirm(request):
    template = 'restaurant/confirmation.html'
    context = {}
    if request.method == 'POST':
        context['name'] = request.POST.get('name', '')
        context['email'] = request.POST.get('email', '')
        context['phone'] = request.POST.get('phone', '')
        context['dishes'] = request.POST.getlist('dishes')
        context['special_dish'] = request.POST.get('special_dish', '')
        context['time'] = datetime.now()
        context['instructions'] = request.POST.get('instructions', '')
    return render(request, template, context)