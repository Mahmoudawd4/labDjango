from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def getAllTodos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def getTodoById(request, id):
    selectedTodo = Todo.objects.get(id=id)
    todoItems = selectedTodo.todoitem_set.all()
    context = {
        'todos': selectedTodo,
        'todoItems': todoItems,
    }
    return render(request, 'tododetails.html', context)

def createTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def updateTodo(request, id):
    selectedTodo = Todo.objects.get(id=id)
    form = TodoForm(instance=selectedTodo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=selectedTodo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
