from django.http import Http404

from .models import Contact
from .serializers import ContactSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Contacts(APIView):

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):

    def get_post(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ContactSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ContactSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)