from django.shortcuts import redirect, render

# Create your views here.
from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.permissions import AllowAny

class TodoItemListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    #permission_classes = [permissions.IsAuthenticated]  # Ensure user is authenticated to access this view
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        
        serializer.save()  # Assign the authenticated user as the owner of the todo item

class TodoItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]# Ensure user is authenticated to access this view
    #permission_classes = [permissions.IsAuthenticated]
    
