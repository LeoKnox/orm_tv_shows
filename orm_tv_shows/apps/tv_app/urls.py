from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_all),
    url(r'^add$', views.add),
    url(r'^add_show$', views.add_show),
    url(r'^display$', views.display),
    url(r'^show_all$', views.show_all),
    url(r'^delete/(?P<my_val>\d+)$', views.delete),
    url(r'^reshow/(?P<my_val>\d+)$', views.reshow),
    url(r'^edit/(?P<my_val>\d+)$', views.edit),
    url(r'^redisplay/(?P<my_val>\d+)$', views.redisplay),
]