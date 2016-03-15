from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^info/$', views.info, name='info'),
    url(r'^postData/$', views.postData, name='postData'),
    url(r'^raspberry/list/$', views.RaspberryListView.as_view(), name='raspberry-list'),
    url(r'^raspberry/(?P<pk>[0-9]+)/$', views.RaspberryDetailView.as_view(), name='raspberry-detail'),
    url(r'^raspberry/(?P<pk>[0-9]+)/data/(?P<name>\w+)$', views.raspberryData, name='raspberry-data'),
    url(r'^raspberry/(?P<pk>[0-9]+)/dataStored/$', views.RaspberryDataStored.as_view(), name='raspberry-data-stored'),
    url(r'^raspberry/(?P<pk>[0-9]+)/led/$', views.LedColorView.as_view(), name='raspberry-led-color'),
]
