from django.urls import path, include
from todolist.views import addTodo, checkedTodo

urlpatterns = [
    path('', addTodo.as_view()),
    path('<int:todo_id>', checkedTodo.as_view())
]
