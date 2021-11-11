from .models import Newsletter
from .serializers import NewsletterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Newsletters(APIView):

    def get(self, request):
        newsletters = Newsletter.objects.all()
        serializer = NewsletterSerializer(newsletters, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
