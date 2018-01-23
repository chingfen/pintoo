from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main2/(?P<main2Id>[0-9]+)/$', views.main2, name='main2'),
    url(r'^commodityCreate/$', views.commodityCreate, name='commodityCreate'),
    url(r'^commodityBuy/(?P<commodityId>[0-9]+)/$', views.commodityBuy, name='commodityBuy'),
]
