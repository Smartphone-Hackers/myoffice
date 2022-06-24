from django.contrib import admin
from officeapp import models

# Register your models here.
admin.site.register(models.StudentModel)
admin.site.register(models.PayeFeesModel)
admin.site.register(models.CourseModel)
admin.site.register(models.CourseTasksModel)
admin.site.register(models.CourseTopicModels)