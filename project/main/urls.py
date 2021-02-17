from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('picture/<int:pk>/', views.detail, name="detail"),
]