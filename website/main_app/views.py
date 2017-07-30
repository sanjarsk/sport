import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

from .models import Active_game
from .forms import ParticipantForm
from .models import Participant

def to_home(request):
    ag = Active_game.objects.filter(date_finish__gte=datetime.datetime.now())
    return render(request, 'home.html', {'active_games': ag})

def show_active_game(request, id):
    game = Active_game.objects.get(id=id)
    sports = game.sports.all()
    context = {'game': game,'sports':sports}
    return render(request, 'show_active_game.html', context)

@login_required
def create_team(request):
    ParticipantFormSet = formset_factory(ParticipantForm, extra=6)

    if request.method == "POST":
        formset = ParticipantFormSet(request.POST)

        if formset.is_valid():
            formset.save()
    else:
        formset = ParticipantFormSet()

    return render(request, "participant_form.html", {"Formset": formset})