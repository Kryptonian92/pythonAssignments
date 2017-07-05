from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^create_team$', views.create_team),
    url(r'^remove$', views.remove),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    # url(r'^current_team/(?P<id>\d+)$', views.current_team)
]
