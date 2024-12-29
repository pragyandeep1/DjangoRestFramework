"""
URL configuration for withrestc2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('api/<int:id>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    # path('api/create/', views.EmployeeCreateAPIView.as_view(), name='employee-create'),
    # path('api/<int:id>/', views.EmployeeRetrieveAPIView.as_view(), name='employee-retrieve'),
    # path('api/<int:id>/', views.EmployeeUpdateAPIView.as_view(), name='employee-update'),
    # path('api/<int:id>/', views.EmployeeDestroyAPIView.as_view(), name='employee-destroy'),
]
