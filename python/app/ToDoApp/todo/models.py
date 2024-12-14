from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.


class TodoModel(models.Model):
    class PriorityType(models.TextChoices):
        HIGH = "1", gettext_lazy("High")
        MEDIUM = "2", gettext_lazy("Medium")
        LOW = "3", gettext_lazy("Low")

    class CompleteType(models.TextChoices):
        INCOMPLETE = "0", gettext_lazy("Incomplete")
        COMPLETE = "1", gettext_lazy("Complete")

    title = models.CharField(max_length=100)
    memo = models.TextField(null=True)
    priority = models.CharField(
        max_length=1, choices=PriorityType.choices, default=PriorityType.MEDIUM
    )
    deadline = models.DateField(null=True)
    complete = models.CharField(max_length=1, choices=CompleteType.choices, default="0")

    def __str__(self):
        return self.title
