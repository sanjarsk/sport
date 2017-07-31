from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', to_home, name='to_home'),
    url(r'^(?P<id>\d+)/$', show_active_game, name='show_active_game'),
    url(r'^team-register/$', ParticipantCreate.as_view(), name='team_register'),

]