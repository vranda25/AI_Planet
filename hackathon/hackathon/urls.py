"""
URL configuration for hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    # signin and login
    path('api/accounts/', include('accounts.urls')),

    # create hackathon and list all hackathons
    path('api/create/', include('create_hack.urls')),

    # register and submit hackathon and list registered and submitted hackathons
    path('api/hackathon/', include('register_submit_hack.urls')),

    # admin panel
    path('admin/', admin.site.urls),
]
