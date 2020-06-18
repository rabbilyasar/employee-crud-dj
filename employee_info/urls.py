from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse

urlpatterns = [
    # path('', HttpResponse('kjfddfk')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),
]
