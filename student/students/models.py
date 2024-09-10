# students/models.py

from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.section}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

