from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    course_fees = models.FloatField()
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

class PayeFeesModel(models.Model):
    name = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    fees_amt = models.FloatField()
    description = models.TextField()

class CourseModel(models.Model):
    name = models.CharField(max_length=100)