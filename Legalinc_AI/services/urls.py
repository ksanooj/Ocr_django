
from django.conf.urls import url
from services.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]