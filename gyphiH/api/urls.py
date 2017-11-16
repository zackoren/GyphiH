from django.conf.urls import url
from .views import getGyphi

urlpatterns = [
    url(r'^gyphi/(?P<location>[\w\+\_\-]{0,25})/(?P<limit>[0-9]{0,20})/$', getGyphi, name="getGyphi"),
]
