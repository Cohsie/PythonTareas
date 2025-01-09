from django.contrib import admin
from django.urls import path
from . import views #Para importar el módulo views que acabo de crear


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
