from django.contrib import admin
from app_td.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)