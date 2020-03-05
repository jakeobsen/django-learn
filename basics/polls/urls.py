from django.urls import path

from . import views

urlpatterns = [
    path('kate/', views.kate, name='kate'),
    path('', views.index, name='index'),
    path('bob/', views.bob, name='bob'),
]