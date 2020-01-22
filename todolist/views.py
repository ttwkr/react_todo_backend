import json

from django.http import JsonResponse
from django.views import View
from .models import TodoList


class addTodo(View):
    def post(self, request):
        data = json.loads(request.body)

        TodoList(
            todo=data['todo']
        ).save()

        return JsonResponse({'result': 'success'}, status=200)
