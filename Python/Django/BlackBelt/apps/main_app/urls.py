from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^add', views.add),
    url(r'^new_trip', views.new_trip),
    url(r'^trip_info/(?P<id>\d+)$', views.trip_info),
    url(r'^join/(?P<id>\d+)$', views.join)

]
