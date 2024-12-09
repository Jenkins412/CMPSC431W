"""
URL configuration for CMPSC431WFinalProject project.

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
from Casino import views

urlpatterns = [
    path('', views.create_account, name='create_account'),
    path('create_account/', views.create_account, name='create_account'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('deposit_money/', views.deposit_money, name='deposit_money'),
    path('join_table/', views.join_table, name='join_table'),
    path('place_bet/', views.place_bet, name='place_bet'),
    path('admin/', admin.site.urls),
]
