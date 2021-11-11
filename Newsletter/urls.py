from django.urls import path
from . import views

urlpatterns = [
    path('', views.Newsletters.as_view(), name='Newsletters'),
]
