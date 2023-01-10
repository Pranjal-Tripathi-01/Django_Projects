from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    age =  models.SmallIntegerField()

    def __str__(self):
        return self.name


    