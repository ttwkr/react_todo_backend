from django.urls import path, include
from todolist.views import addTodo, checkedTodo, deleteTodo

urlpatterns = [
    path('', addTodo.as_view()),
    path('<int:todo_id>', checkedTodo.as_view()),
    path('delete/<int:todo_id>', deleteTodo.as_view())
]
