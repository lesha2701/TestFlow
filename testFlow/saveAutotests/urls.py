from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_autotests/', views.save_autotests, name='save_autotests'),
]