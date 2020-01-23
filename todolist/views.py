import json

from django.http import JsonResponse
from django.views import View
from .models import TodoList


class addTodo(View):
    def post(self, request):
        data = json.loads(request.body)

        TodoList(
            todo=data['todo'],
            check=data['check']
        ).save()

        return JsonResponse({'result': 'success'}, status=200)

    def get(self, request):

        TodoLists = TodoList.objects.all()
        return JsonResponse({'result': list(TodoLists.values())})


class checkedTodo(View):
    def post(self, request, todo_id):

        data = json.loads(request.body)

        todo = TodoList.objects.get(id=todo_id)
        todo.check = data['check']
        todo.save()

        return JsonResponse({'result': 'success'}, status=200)
