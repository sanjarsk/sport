import datetime
from django.shortcuts import render

from django.views.generic.edit import CreateView

from .models import Active_game
from .forms import ParticipantForm
from .models import Participant, Sport

def to_home(request):
    ag = Active_game.objects.filter(date_finish__gte=datetime.datetime.now())
    return render(request, 'home.html', {'active_games': ag})

def show_active_game(request, id):
    game = Active_game.objects.get(id=id)
    sports = game.sports.all()
    context = {'game': game,'sports':sports}
    return render(request, 'show_active_game.html', context)

class ParticipantCreate(CreateView):
    form_class = ParticipantForm
    template_name = "participant_form.html"



