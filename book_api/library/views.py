
from django.shortcuts import render
from rest_framework import generics
from library.models import Book
from library.serializers import BookSerializers

class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializers

class BookDetails(generics.RetrieveUpdateAPIView):
    queryset=Book
    serializer_class=BookSerializers

