from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': True},  # Set title field as required
            'description': {'required': False},  # Set description field as not required
              # Set user field as not required
        }
