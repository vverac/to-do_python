from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoList, ToDoItem

class List_view(ListView):
    model = ToDoList
    template_name = "app_td/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "app_td/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context