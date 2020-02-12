from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('click_button', views.click_button),
    path('reset', views.reset),
]
