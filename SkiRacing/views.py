from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from SkiRacing.models import Racer, Competition
# Create your views here.


def hello(request):
    return HttpResponse('Hello Ivan')


def racers(request):
    racers_arr = Racer.objects.all()
    template = loader.get_template('racer/index.html')
    context = {
        'racers': racers_arr,
    }
    return HttpResponse(template.render(context))


def racer(request):
    racer_temp = Racer.objects.get(id=request.GET['id'])
    template = loader.get_template('racer/main.html')
    context = {
        'racer': racer_temp,
    }
    return HttpResponse(template.render(context))


def competitions(request):
    competitions_arr = Competition.objects.all()
    template = loader.get_template('competition/index.html')
    context = {
        'competitions': competitions_arr,
    }
    return HttpResponse(template.render(context))


def competition(request):
    competition_temp = Competition.objects.get(id=request.GET['id'])
    template = loader.get_template('competition/main.html')
    context = {
        'competition': competition_temp,
    }
    return HttpResponse(template.render(context))