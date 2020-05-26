from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index', views.index, name='user_index'),
    path('add', views.add, name='user_add'),
    path('detail/<id>', views.detail, name='user_detail'),
    path('checkCode/<code>', views.check_code, name='user_check_code'),
    path('checkTel/<tel>', views.check_tel, name='user_check_tel'),
    path('del/<id>', views.delete, name='del_user'),
    path('update/<id>', views.update, name='user_update'),
    path('search', views.search, name='user_search'),
]
