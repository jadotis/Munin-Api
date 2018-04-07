from django.conf.urls import url
from . import views

urlpatterns = [
    url('list', views.returnImagesList),
    url(r'', views.index)
]