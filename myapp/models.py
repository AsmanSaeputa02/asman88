from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name+","+ str(self.age)