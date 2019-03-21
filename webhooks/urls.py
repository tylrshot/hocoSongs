from django.urls import path

from . import views

app_name = 'webhooks'
urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('inbound-sms', views.inbound, name='inbound'),
    
    path('inbound-view', views.inboundView, name='inboundView'),
    
    path('songs', views.inboundView, name='renderView'),
    
    path('songAdmin', views.songAdmin, name='songAdmin'),
    
    path('fast', views.fast, name='fast'),
    path('slow', views.slow, name='slow'),
    path('dance', views.dance, name='dance'),
    path('other', views.other, name='other'),
    path('christmas', views.christmas, name='christmas'),
    
    path('reset81273', views.reset81273, name='reset81273'),

]