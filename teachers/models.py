from django.db import models
from user.models import User
# Create your models here.

class Teachers(models.Model):

    id = models.AutoField(primary_key=True, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=320, null=False, blank=False)
    subjects = models.CharField(max_length=320, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_activate = models.BooleanField(default=True)

    class Meta: 
        db_table = "teachers"

    def __str__(self):
        return self.teacher_name