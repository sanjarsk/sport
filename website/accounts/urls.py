from django.conf.urls import url
from accounts.views import *


urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'^auth/$', auth_view, name='auth_view'),
    url(r'^logout/$', logout, name='logout'),
]