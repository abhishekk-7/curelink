from django.shortcuts import render
from .serializers import ContentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from account.models import UserModel

# Create your views here.


class ContentView(GenericAPIView):
    serializer_class = ContentSerializer

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendEmailView(GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, request):
        print(request.data)
        return Response(UserModel.objects.filter(subscription=request.data['topic']).values('email'), status=status.HTTP_200_OK)
