from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

# Create your views here.

@api_view(['GET'])
def student_list(request):
    
    students = Student.objects.all()
    
    serializer = StudentSerializers(students,many=True)
    
    return Response(serializer.data)


