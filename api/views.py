from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication,permissions
from api.serializers import *
from django.db.models import Sum

# Create your views here.

class CustomerViewSetView(ModelViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerilizer

    def perform_create(self, serializer):
        serializer.save(technician=self.request.user)