from django.conf.urls import url
from . import views

urlpatterns = [
    url('list', views.returnImagesList),
    url('elements', views.returnElements),
    url(r'', views.index)
]