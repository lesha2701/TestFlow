from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_autotests/', views.save_autotests, name='save_autotests'),
    path('run_autotest/<int:test_id>/', views.run_autotest, name='run_autotest'),
    path('see_autotest/<int:test_id>/', views.see_autotest, name='see_autotest'),
]