"""sportify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from sportifyapp.views import (
    HomeView,
    TeamView,
    SportView,
    JucatorCreate,
    JucatorUpdate,
    JucatorDelete
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sports/<int:sport_id>', SportView.as_view(), name = 'sports'),
    path('teams/<int:team_id>', TeamView.as_view(), name='teams'),
    path('jucator/create/', JucatorCreate.as_view(), name='jucator-create'),
    path('jucator/<int:pk>/update/', JucatorUpdate.as_view(), name='jucator-update'),
    path('jucator/<int:pk>/delete/', JucatorDelete.as_view(), name='jucator-delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
