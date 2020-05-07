"""recipebox URL Configuration

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
from django.urls import path

from recipe.urls import urlpatterns as recipe_urls
from recipe import views

urlpatterns = [
    # path('', views.index)
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
    path('add_author/', views.add_author, name="add_author"),
    path('author/<int:id>/', views.author, name='author'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout, name='logout'),
]
urlpatterns += recipe_urls