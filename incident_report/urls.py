from incident_report import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^/receiveReport/$',views.receive_incident, name='report' ),
    url(r'^/map/$', views.show_map, name='map'),
    url(r'^/report/$', views.lol, name='lol'),
    url(r'^/incident/$', views.incident, name='incident'),

)