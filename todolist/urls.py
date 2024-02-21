from django.urls import path
from .views import TodoItemListCreateAPIView, TodoItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', TodoItemListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoItemRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),
]
