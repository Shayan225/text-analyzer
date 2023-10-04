from django.contrib import admin
from django.urls import path
from text import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('Analyze/',views.Analyze, name='Analyze'),
]
