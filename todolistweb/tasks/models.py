from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    compile = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title