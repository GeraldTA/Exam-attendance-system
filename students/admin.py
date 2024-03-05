from django.contrib import admin

from .models import Submission,Student_details,Course_details,Exam_details,Register

# Register your models here.
admin.site.register(Submission)
admin.site.register(Student_details)
admin.site.register(Course_details)
admin.site.register(Exam_details)
admin.site.register(Register)


