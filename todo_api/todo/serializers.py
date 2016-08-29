from rest_framework import serializers
from todo_api.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'description',
            'done'
        )
