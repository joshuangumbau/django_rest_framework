# Create your models here.
#name and alias are character fields where we can store strings.
# The __str__ method just tells Django what to print when it needs to print out an instance of the Hero model.

from django.db import models

class hero(models.Model):
    name = models.CharField(max_length = 60)
    alias = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.name
    
    