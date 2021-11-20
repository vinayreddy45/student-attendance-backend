from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    SECTION = (
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('MEC', 'MEC'),
        ('IT', 'IT'),
        ('CSE', 'CSE'),
    )
    name = models.CharField(max_length=50)
    rollNo = models.CharField(max_length=10, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='student_list')

    def __str__(self):
        return self.rollNo

class Subject(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ':' + str(self.date)
    
    class Meta:
        unique_together = ['name', 'branch']

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_list')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance_list')
    isPresent = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.student) + ":" + str(self.subject)

@receiver(post_save, sender=Subject)
def create_attendance_list(sender, instance, created, **kwargs):
    if created:
        for student in Student.objects.filter(branch=instance.branch):
            attendance = Attendance(
                student=student,
                subject=instance,
                isPresent=False,
                branch=instance.branch
            )
            attendance.save()