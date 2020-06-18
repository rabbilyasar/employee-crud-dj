from django.contrib import admin
from django.urls import path

from . import views

app_name = "employee_register"

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('form', views.employee_form, name='employee_form'),
    path('<int:pk>/delete', views.employee_delete, name='employee_delete'),
    path('<int:pk>/update', views.employee_form, name='employee_update'),

]
