"""
URL configuration for Education_django_HW project.

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
from course import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('topic_list/', views.topic_list_view),
    path('topic_create/', views.create_topic_view),
    path('topic_detail_view/<int:pk>', views.detail_view),
    path('topic_update/update/<int:pk>', views.topic_update),
    path('topic_del/<int:pk>', views.topic_del)
]

