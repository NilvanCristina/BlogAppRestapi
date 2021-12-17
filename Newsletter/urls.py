from django.urls import path
from . import views

urlpatterns = [
    path('data', views.Newsletters.as_view(), name='Newsletters'),
    path('<int:pk>', views.NewsletterDetails.as_view(), name='NewsletterDetail'),
]
