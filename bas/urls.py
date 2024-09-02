from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name="admin_home"),
    path('empresa/edit/', empresa_edit, name='empresa_edit'),

    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]