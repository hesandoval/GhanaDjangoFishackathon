from incident_report import views
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^/receiveReport/$',views.receive_incident, name='report' ),
    url(r'^/map/$', views.show_map, name='map'),
    url(r'^/report/$', views.lol, name='lol'),
    url(r'^/incident/$', views.incident, name='incident'),

)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )