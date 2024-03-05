from django.db import models
from django.utils import timezone
import qrcode
import os
from io import BytesIO
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw




class Submission(models.Model):
    studentname = models.CharField(max_length=400)
    studentId = models.CharField(max_length=300)
    examdate = models.DateTimeField()
    attended = models.BooleanField()
    submitted = models.BooleanField()
    signature = models.TextField(default="In prgress, comming soon", max_length=100)
       
    def __str__(self):
        return f"{self.exam.course_id.name}"

class Course_details(models.Model):
    CourseID = models.CharField(max_length=300, unique=True)
    name= models.CharField(max_length=300)
    year_taken = models.IntegerField()
    department_id= models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Exam_details(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    course_id = models.ForeignKey(Course_details, on_delete=models.CASCADE, limit_choices_to={'year_taken': timezone.now().year})
    number_of_students = models.IntegerField()
    invigilator = models.CharField(max_length=300)
     
    def __str__(self):
        return f"{self.course_id.name} - {self.date}"
    
    
class Student_details(models.Model):
    student_id = models.CharField(max_length=400)
    name= models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    program=models.CharField(max_length=300, null =True)
    year= models.CharField(max_length=300) 
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
    
      
    def save(self,*args, **kwargs):
       qrcode_img = qrcode.make(self.student_id)
       canvas= Image.new('RGB', (290,290), 'white') 
       draw = ImageDraw.Draw(canvas)
       canvas.paste(qrcode_img)
       fname=f'qr_code-{self.student_id}'+'.png'
       buffer = BytesIO()
       canvas.save(buffer,'PNG')
       self.qr_code.save(fname, File(buffer), save=False)
       canvas.close()
       super().save(*args, **kwargs)
             
        
    def __str__(self):
        return f"{self.name} {self.surname} "

class Register(models.Model):
    student_id = models.ForeignKey(Student_details, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Exam_details, on_delete=models.CASCADE, limit_choices_to={'date__gte': timezone.now()}, null=True, blank=True)
    attended = models.BooleanField(default=False)
    signature = models.TextField(default="In prgress, comming soon", max_length=100)
       
    
    
       
