from django.urls import path
from .views import getAllTodos, getTodoById, createTodo, updateTodo, deleteTodo

urlpatterns = [
    path('', getAllTodos),
    path('todos/<str:id>', getTodoById, name='todos'),
    path('create/', createTodo, name='create'),
    path('update/<str:id>', updateTodo, name='update'),
    path('delete/<str:id>', deleteTodo, name='delete'),

]
