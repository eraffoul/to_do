from rest_framework import serializers

from .models import ToDo

class ToDoSerializerGet(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('description', 'created_at', 'id')

class ToDoSerializerPost(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = [('description')]

class ToDoSerializerDel(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = [('id')]

class ToDoSerializerDetail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id','description','created_at')