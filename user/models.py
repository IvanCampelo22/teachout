from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=420, null=False)
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=True)

    class Meta:
        db_table = "user"
        unique_together = ["email", "username"]
        ordering = ["created_at"]

    def __str__(self):
        return self.email