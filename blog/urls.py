from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item_detail'),
    url(r'^item/(?P<pk>[0-9]+)/edit/$', views.item_edit, name='item_edit'),
]