"""patt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from apparm import views

urlpatterns = [
    #path to access page admin
    path('admin/', admin.site.urls),
    # path to render home
    path('', views.frontend, name='frontend'),
    # path login/logout
    path('login/', include('django.contrib.auth.urls')),

    #==================
    #BACKEND SECTION
    #path to access the backend page
    path('backend/', views.backend, name='backend'),
    #path to add proveedor
    path('add_proveedor', views.add_proveedor, name="add_proveedor"),

    #path to delete proveedor
    path('delete_proveedor/<str:pro_id>', views.delete_proveedor, name="delete_proveedor"),
    #path to access the proveedor individual
    path('provee/<str:pro_id>', views.provee, name='provee'),
    #path to edit the proveedor 
    path('edit_proveedor', views.edit_proveedor, name='edit_proveedor'),

    #Support
    path('support', views.support, name='support'),
]
