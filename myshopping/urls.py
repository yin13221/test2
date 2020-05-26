"""myshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    url("^$", views.login, name="login"),
    url("^user/", include("user.urls")),
    url("^bill/", include("bill.urls")),
    url("^sup/", include("supplier.urls")),
    path('billList', views.billList, name="billList"),
    path("providerlist", views.providerlist, name="providerlist"),
    path("change_pwd", views.change_pwd, name="change_pwd"),
    path('logout', views.logout, name='logout'),
]
