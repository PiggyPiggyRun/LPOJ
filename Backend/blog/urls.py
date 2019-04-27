# -*- coding: utf-8 -*-


from django.conf.urls import url,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('ojmessage', views.OJMessageView)
routers.register('blog', views.BlogView)

urlpatterns = [
    url('', include(routers.urls)),
]
