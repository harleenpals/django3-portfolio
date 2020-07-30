from django.db import models

class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.tittle
