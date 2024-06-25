from django.db import models
from student.models import Student
from teachers.models import Teachers

class Classes(models.Model):
    
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
    
    HIGHSCOOL = "HS"
    UNIVERSITY = "UNI"
    TEACHING_LEVEL = {
        HIGHSCOOL: "High School",
        UNIVERSITY: "University",
    }

    id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    subject = models.CharField(max_length=8, choices=SUBJECTS_CHOICES, null=False)
    class_level = models.CharField(max_length=3, choices=TEACHING_LEVEL,null=False)
    value_by_hour = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "classes"
        ordering = ["created_at"]


class RequestClasses(models.Model):

    id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "request_classes"
        ordering = ["created_at"]
