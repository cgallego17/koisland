from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="admin_home"),
    path('empresa/edit/', empresa_edit, name='empresa_edit'),


]