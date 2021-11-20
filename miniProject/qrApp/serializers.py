from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Student, Attendance, Subject

class StudentSerializer(ModelSerializer):
    branch = ReadOnlyField(source="branch.name")
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(ModelSerializer):
    student = ReadOnlyField(source='student.rollNo')
    subject = ReadOnlyField(source='subject.name')
    class Meta:
        model = Attendance
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']