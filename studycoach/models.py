from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title

# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     deadline = models.DateField()
#     is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

