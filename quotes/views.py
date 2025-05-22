from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random

Quotes = ["All political power comes from the barrel of a gun. The communist party must command all the guns, that way, no guns can ever be used to command the party.", "When there is not enough to eat, people starve to death. It is better to let half of the people die so that the other half can eat their fill.","A revolution is not a dinner party, or writing an essay, or painting a picture, or doing embroidery; it cannot be so refined, so leisurely and gentle, so temperate, kind, courteous, restrained and magnanimous. A revolution is an insurrection, an act of violence by which one class overthrows another.", "Revolutionary culture is a powerful revolutionary weapon for the broad masses of the people. It prepares the ground ideologically before the revolution comes and is an important, indeed essential, fighting front in the general revolutionary front during the revolution. "]

Pics = ["https://upload.wikimedia.org/wikipedia/commons/7/7e/Mao_Zedong_in_1957_%28cropped%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/0/0b/Mao_Zedong_sitting.jpg", "https://upload.wikimedia.org/wikipedia/commons/2/21/Mao_Zedong_and_Zhang_Yufeng_in_1964.jpg", "https://www.futuresforextrading.com/renminbi/renminbi-100-new-front.jpg"]

# Create your views here.
def home(request):
    template = 'quotes/quote.html'
    context = {
        'quote': random.choice(Quotes),
        'url': random.choice(Pics)
    }
    return render(request, template, context)



def show_all(request):
    
    template = 'quotes/show_all.html'
    context = {
        'quotes': Quotes,
        'pics': Pics
    }

    return render(request, template, context)
def about(request):
    template = 'quotes/about.html'
    context = {
        'name': 'John Doe',
        'bio': 'A passionate developer and quote enthusiast.'
    }
    return render(request, template, context)

