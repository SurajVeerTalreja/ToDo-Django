from django.shortcuts import render
from .models import ToDoList
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def home(request):
    return render(request, 'dashboard/home.html')

class ToDoCreate(CreateView):
    # Connect it with a model of your choice
    model = ToDoList

    # Tell it what fields you require in form inside model_form.html (teacher_form.html)
    # After user hits a submit button, it creates and saves an instance of model in database auto.
    fields = '__all__'

    # Redirecting to a page
    success_url = reverse_lazy('todo_list')


class ToDoListView(ListView):
    model = ToDoList

    context_object_name = 'todo_list'

class DetailListView(DetailView):
    # Return ONLY ONE model Entry   
    # It looks for model_detail.html
    model = ToDoList

    
class UpdateList(UpdateView):
    # Connect it with a model of your choice
    # Shares the same template as CreateView
    model = ToDoList

    # Tell it what fields you require in form inside model_form.html (teacher_form.html)
    # After user hits a submit button, it updates and saves an instance of model in database auto.
    fields = '__all__'

    # Redirecting to a page
    success_url = reverse_lazy('todo_list')

class DeleteEntry(DeleteView):
        # Form --> Confirm Delete Button
    # Default Template: model_confirm_delete.html
    model = ToDoList

    success_url = reverse_lazy('todo_list')