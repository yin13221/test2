from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("billAdd", views.billAdd, name='billAdd'),
    path('billUpdate/<int:pk>', views.billUpdate, name='billUpdate'),
    path('billView/<int:pk>', views.billView, name='billView'),
    path('query', views.query, name='query'),
    path('dele/<int:id>',views.dele,name='dele'),
    path('check/<code>', views.check_code, name='check_code'),
]
