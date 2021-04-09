from django.db import models

class Plane(models.Model):
    name = models.CharField(max_length=50)
    adding_date = models.DateField(auto_now=False)
    descr = models.TextField(default="No description for this plane")

    def __str__(self):
        return self.name
