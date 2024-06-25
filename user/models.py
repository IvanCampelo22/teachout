from django.db import models

class User(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=420, null=False)
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=120, null=False)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    class Meta:
        db_table = "user"
        unique_together = ["email", "username"]
        ordering = ["created_at"]
