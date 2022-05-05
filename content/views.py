from django.shortcuts import render
from .serializers import ContentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from account.models import UserModel
from django.conf import settings
from django.core.mail import send_mail

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
        try:
            subject = request.data['subject']
            message = request.data['content']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = []
            to_mails = UserModel.objects.filter(
                topic=request.data['topic']).values('email').distinct()
            for mail in to_mails:
                recipient_list.append(mail['email'])
            send_mail(subject, message, email_from, recipient_list)
            return Response("success", status=status.HTTP_200_OK)
        except:
            return Response("failed", status=status.HTTP_400_BAD_REQUEST)
