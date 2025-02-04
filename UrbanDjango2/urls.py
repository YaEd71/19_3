"""
URL configuration for UrbanDjango2 project.

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
from task1 import views as task1_views

urlpatterns = [
    path('', task1_views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up', task1_views.sign_up_by_django, name='sign_up_by_django'),
    path('admin/', admin.site.urls),
    path('platform/', task1_views.platform, name='platform'),
    path('platform/games/', task1_views.games, name='games'),
    path('platform/cart/', task1_views.cart, name='cart'),
]
