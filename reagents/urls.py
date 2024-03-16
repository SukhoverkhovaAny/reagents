from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('content/', views.content, name='content'),
    path('user_content/', views.user_content, name='user_content'),
    path('show_petr_ether/', views.show_petr_ether, name='show_petr_ether'),
    path('user_show_petr_ether/', views.user_show_petr_ether, name='user_show_petr_ether'),
    path('show_chloro/', views.show_chloro, name='show_chloro'),
    path('user_show_chloro/', views.user_show_chloro, name='user_show_chloro'),
    path('show_silica/', views.show_silica, name='show_silica'),
    path('user_show_silica/', views.user_show_silica, name='user_show_silica'),
    path('show_naoh/', views.show_naoh, name='show_naoh'),
    path('user_show_naoh/', views.user_show_naoh, name='user_show_naoh'),
    path('user_autho_form/', views.user_autho_form, name='user_autho_form'),
    path('add_consumption_form/<int:id_reagent>', views.add_consumption_form, name='add_consumption_form'),
]
