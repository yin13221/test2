from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("provideradd", views.provideradd, name="provideradd"),
    url("providerupdate/(?P<pk>\d+)", views.providerupdate, name="providerupdate"),
    url("providerview/(?P<pk>\d+)", views.providerview, name="providerview"),
    path("check/<tel>", views.check_tel, name="check"),

    path("search", views.search, name="search"),
    path("del/<int:id>", views.delete, name="delete")

]
