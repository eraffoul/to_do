from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ToDoForm
from .models import ToDo
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ToDoSerializerGet
from .serializers import ToDoSerializerPost
from .serializers import ToDoSerializerDel
from .serializers import ToDoSerializerDetail



def addToDo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'The ToDo was successfully created')
            return redirect('index')
    else:
        form = ToDoForm()

    return render(request, 'add.html', {'form': form})


def index(request):
    sort_by = request.GET.get('sort_by')
    order = request.GET.get('order_by')

    # Defines how is going to be the description and created_at sorting link at the index page
    desc_order,created_order = 'asc','asc'

    if (sort_by == 'description'):
        if (order == 'desc'):
            todo_list = ToDo.objects.order_by('-description')
        else:
            desc_order = 'desc'
            todo_list = ToDo.objects.order_by('description')

    elif (sort_by == 'created_at'):

        if (order == 'desc'):
            todo_list = ToDo.objects.order_by('-created_at')

        else:
            created_order = 'desc'
            todo_list = ToDo.objects.order_by('created_at')

    else:
        todo_list = ToDo.objects.order_by('id')

    return render(request, 'index.html', {'todo_list': todo_list, 'desc_order':desc_order, 'created_order':created_order})

def detail(request, todo_id):
    todo = get_object_or_404(ToDo,id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def remove(request,todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.delete()
    messages.add_message(request, messages.INFO, 'The ToDo was successfully removed')
    return redirect('index')


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()

    serializer_class = ToDoSerializerDetail

    action_serializers = {
        'list': ToDoSerializerGet,
        'create': ToDoSerializerPost,
        'retrieve': ToDoSerializerDetail,
        'update': ToDoSerializerDetail,
        'delete': ToDoSerializerDel
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializer'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ToDoViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
