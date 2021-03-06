from django.db import models
from django.utils import timezone

import datetime

class TodoItem(models.Model):
    """
    This can be done with a single model TodoItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.
    """
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=True)
    completed_date = models.DateTimeField(null=True)
    completed_bool = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.text}, Created: {self.created_date}, Completed: {self.completed_bool} on {self.completed_date}"