from django.test import TestCase
from django.db import models
from django.utils.translation import gettext_lazy
# Create your tests here.
class TodoModel(models.Model):
    class PriorityType(models.TextChoices):
        HIGH = '1',gettext_lazy('High')
        MEDIUM= '2', gettext_lazy('Medium')
        LOW = '3', gettext_lazy("Low")

a = TodoModel.PriorityType.HIGH

print(a)



