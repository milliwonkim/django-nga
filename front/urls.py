from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('front/main', views.front_main, name="front_main"),

    path('front/main/<int:pk>',views.front_detail, name='front_detail'),

    path('front/write',views.front_write,name='front_write'),
    path('front/create',views.front_create,name='front_create'), 
    path('front/edit<int:pk>',views.front_edit,name='front_edit'),
    path('front/update<int:pk>',views.front_update,name='front_update'),
    path('front/delete<int:pk>',views.front_delete,name='front_delete'),

]