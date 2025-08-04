from django.db import models

class agenda(models.Model): 
    tarefa = models.CharField(max_length=50)
    data = models.DateField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tarefa