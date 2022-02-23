from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q
import datetime

from .models import Attendance, Student, Subject
from .serializers import AttendanceSerializer, StudentSerializer, SubjectSerializer

class SubjectListAPI(APIView):

    def get(self, request):
        q = Q(date=datetime.date.today())
        subjects = Subject.objects.filter(q)

        query = request.GET.get("semester")
        if query:
            subjects = subjects.filter(semester=int(query))

        serializer = SubjectSerializer(subjects, many=True)

        return Response(serializer.data)

class AddAttandanceAPI(APIView):

    def post(self, request):
        data = request.data

        rollNo = data['rollNo']
        subject = data['subject']

        print(rollNo)

        student = Student.objects.get(rollNo=rollNo)


        q1 = Q(name=subject)
        q2 = Q(date=datetime.date.today())

        attendance = student.attendance_list.get(subject=Subject.objects.get(q1 & q2))
        attendance.isPresent = True
        attendance.save()

        student = StudentSerializer(student)
        attendance = AttendanceSerializer(attendance)

        return Response({
            'message': 'attendance is created successfully',
            'student': student.data,
            'attendance': attendance.data
        })

class AttendanceListAPI(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer