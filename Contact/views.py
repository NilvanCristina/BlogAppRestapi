from .models import Contact
from .serializers import ContactSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Contacts(APIView):

    def get(self, request):
        contacts = Contact.objects.all()
