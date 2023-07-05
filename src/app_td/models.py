from django.db import models
from django.utils import timezone
from django.db import models
from django.urls import reverse

#  se define una función que dvuelve la hora actual mas un delta de 7 dias
def one_week():
    return timezone.now() + timezone.timedelta(days=7)
#  defino 2 modelos:
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    # esta clase ordena segun la fecha de vencimiento
    class Meta:
        ordering = ["due_date"]