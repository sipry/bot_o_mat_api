from django.urls import path
from robots import views

urlpatterns = [
    path('robots/', views.robot),
    path('robots/<int:robot_pk>/', views.robot),
]