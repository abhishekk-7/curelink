from django.shortcuts import render
from rest_framework.response import Response
from .serializers import SubscriptionSerializer
from rest_framework.generics import GenericAPIView
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request):
        print(request.data)
        serializer = SubscriptionSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
