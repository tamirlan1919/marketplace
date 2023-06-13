"""
URL configuration for market project.

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
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main' ),
    path('clothes/<int:id_clothes>/',views.show_sub_tovar,name = 'show_tovar'),
    path('products/<int:cat_id>/', views.products_by_category_view, name='products_by_category'),
    path('login/',views.user_login,name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('form/', views.index, name = 'index'), 
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('user/profile/',views.profile_user,name='profile_user'),
    path('cart/',views.cart,name='cart'),
    path('like/',views.likes, name='likes'),
    path('order/',views.order,name='order'),
    path('checkout/',views.checkout, name='checkout')


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)