from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'config/', views.return_config),
    url(r'modules/', views.modules)
]