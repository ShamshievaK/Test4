"""
URL configuration for ToDoList project.

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
from tasks.views import mane_page_view, task_list_view, task_detail_view, task_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', mane_page_view),
    path('tasks/', task_list_view),
    path('tasks/<int:id>/', task_detail_view),
    path('tasks/create/', task_create_view),
]
