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


class Curriculum(models.Model):

    BIOLOGY = "BIO"
    MATH = "MATH"
    CHEMISTRY = "CHEM"
    PHYSICS = "PHYSC"
    ENGLISH = "ENG"
    SUBJECTS_CHOICES = {
        BIOLOGY: "Biology",
        MATH: "Mathematics",
        CHEMISTRY: "Chemistry",
        PHYSICS: "Physics",
        ENGLISH: "English",
    }
    id = models.AutoField(primary_key=True, null=False)
    description = models.TextField(null=False)
    subject = models.CharField(max_length=8, choices=SUBJECTS_CHOICES, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta: 
        db_table = "curriculum"

    def __str__(self):
        return self.description


class Academic(models.Model):

    id = models.AutoField(primary_key=True, null=False)
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    degree_title = models.TextField(null=False)
    degree_url = models.TextField(null=False)
    image = models.ImageField(null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta: 
        db_table = "academics"

    def __str__(self):
        return self.degree_title
