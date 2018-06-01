from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductListSerializer
from .models import Productlist

class ProductListDetailsView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Productlist.objects.all()
    serializer_class = ProductListSerializer 
