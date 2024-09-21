from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='home.html'), name='home'),  
    path('register/', views.register, name='register'), 
    path('post_list', views.post_list, name='post_list'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  
    path('contact/', views.contact_view, name='contact'), 
    path('admin/', admin.site.urls), 
]