from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='CultureBox-home'),
    path('about/', views.about, name='CultureBox-about'),
]
