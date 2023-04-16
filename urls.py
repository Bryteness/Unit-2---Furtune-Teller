from django.urls import path

from . import views

app_name = 'Fortune_Teller'
urlpatterns = [
    path('', views.index, name='index'),
]