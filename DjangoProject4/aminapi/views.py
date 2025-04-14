from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from aminapi.models import Contact
from aminapi.serializers import ContactSerializer


# Create your views here.
class GenericAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class GenericCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobile_number')

        if not mobile_number:
            return Response({"error": "mobile_number required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Contact.objects.get(mobile_number=mobile_number)
        except Contact.DoesNotExist:
            return Response({"error": "mobile_number not found"}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken()
        refresh['user_id'] = user.id
        refresh["name"] = user.name

        access = refresh.access_token

        return Response({
            'refresh' : str(refresh),
            'access' : str(access),
            'user_id':user.id
        })


