from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from SkiRacing.models import Racer, Competition, Race
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
    comps = [Competition.objects.get(id = temp.competition_id_id) for temp in Race.objects.filter(racer_id_id = racer_temp.id)]
    template = loader.get_template('racer/main.html')
    context = {
        'racer': racer_temp,
        'competitions': comps,
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
    racers_arr = [Racer.objects.get(id=temp.racer_id_id) for temp in Race.objects.filter(competition_id_id=competition_temp.id)]
    template = loader.get_template('competition/main.html')
    context = {
        'competition': competition_temp,
        'racers': racers_arr,
    }
    return HttpResponse(template.render(context))


def racer_in_competition(request):
    race = Race.objects.get(racer_id_id = request.GET['racer_id'], competition_id_id = request.GET['competition_id'])
    racer_temp = Racer.objects.get(id = request.GET['racer_id'])
    competition_temp = Competition.objects.get(id = request.GET['competition_id'])
    template = loader.get_template('racer_in_competition/index.html')
    context = {
        'competition': competition_temp,
        'racer': racer_temp,
        'race': race,
    }
    return HttpResponse(template.render(context))