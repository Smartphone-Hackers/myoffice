from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    email = models.EmailField()
    course_fees = models.FloatField()
    address = models.TextField(null=True)
    photo = models.URLField(null=True)

    def __str__(self):
        return f"{self.name}"

class PayeFeesModel(models.Model):
    name = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    fees_amt = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name.name} -> {self.fees_amt}"

class CourseModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class CourseTopicModels(models.Model):
    name = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    topic = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name.name} -> {self.topic}"

class CourseTasksModel(models.Model):
    topics = models.ForeignKey(CourseTopicModels, on_delete=models.CASCADE)
    question = models.TextField()
    sample_input = models.TextField(null=True)
    sample_output = models.TextField(null=True)

    def __str__(self):
        return f"{self.topics.name.name} -> {self.question}"