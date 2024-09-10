from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('export_pdf/<int:pk>/', views.export_student_pdf, name='export_student_pdf'),
]
