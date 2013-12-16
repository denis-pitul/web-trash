from django.conf.urls import patterns, url
from log import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^new$', views.new, name='new'),
        url(r'^add$', views.add, name='add'),
        url(r'^view$', views.view, name='view'),
)
