from django.urls import path
from django.urls.conf import include
from .views import indexView, notificationView
urlpatterns = \
[
    path('', indexView,name = "index"),
    path('notification', notificationView,name = "notification"),
]