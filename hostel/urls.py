"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import (index, detail, get_records,get_data_by_id)
from django.urls import path

urlpatterns = [
    path('index/', index, name='indexx'),
    path('detail/<int:pk>',detail , name='detail'),
    path('records/<int:no_of_records>',get_records , name='detail'),
    path('record_by_id/<int:id>',get_data_by_id , name='one_result'),
]
