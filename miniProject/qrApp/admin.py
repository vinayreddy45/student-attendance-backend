from django.contrib import admin
from .models import Student, Attendance, Subject, Branch
# Register your models here.

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Subject)
admin.site.register(Branch)