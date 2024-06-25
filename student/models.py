from django.db import models
from user.models import User

class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_high_school = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    class Meta:
        db_table = "student"
        ordering = ["created_at"]
