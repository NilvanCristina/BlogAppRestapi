from django.urls import path
from . import views

urlpatterns = [
    path('data', views.Contacts.as_view(), name='Contacts'),
    path('<int:pk>', views.ContactDetails.as_view(), name='ContactDetail'),
]
