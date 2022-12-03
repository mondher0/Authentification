from django.urls import path 
from .import views

urlpatterns=[
    path('front', views.frontpage, name='front'),
    path('log_in', views.login, name='log_in'),
    path('sign_up', views.signup, name='sign_up'),
    path('logout',views.logout,name='logout'),
]