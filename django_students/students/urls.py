from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student),
    path('', views.get_all_students),
    path('<int:pk>/', views.get_student),
    path('update/<int:pk>/', views.update_student),
    path('delete/<int:pk>/', views.delete_student),
]
