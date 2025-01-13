from django.db import models

# Create your models here.
class CourseData(models.Model):
    course_no=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=20)
    course_timings=models.CharField(max_length=20)
    course_duration=models.CharField(max_length=20)
    course_startdate=models.DateField()
    course_fee=models.IntegerField()
    trainer_name=models.CharField(max_length=20,default='Unknown')

class FeedbackData(models.Model):
    name=models.CharField(max_length=20)
    rating=models.IntegerField()
    comment=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
