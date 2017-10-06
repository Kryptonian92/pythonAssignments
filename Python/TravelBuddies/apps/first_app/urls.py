from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^travels$', views.travels),
    url(r'^travels/add$', views.add),
    url(r'^travels/new_trip$', views.new_trip),
    url(r'^travels/logout$', views.logout),
    # url(r'^travels/success$', views.success),

    ]
