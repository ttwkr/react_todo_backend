from django.db import models


class TodoList(models.Model):
    todo = models.CharField(max_length=400)
    check = models.BooleanField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todolists'
