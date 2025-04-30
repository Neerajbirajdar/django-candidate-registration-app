from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
@api_view(['POST'])
def add(request):
    if request.method=='POST':
        data=StudentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)

@login_required
@api_view(['POST'])
def update(request):
    if request.method=='POST':
        stu_id=request.data.get('id')
        try:
            stu=Student.objects.get(stu_id)
        except:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        
        stu_serializer=StudentSerializer(stu,data=request.data, partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(stu_serializer.data, status=status.HTTP_200_OK)
        return Response(stu_serializer.errors)

@login_required
@api_view(['GET'])
def get_all(request):
    if request.method=='GET':
        student_data=Student.objects.all()
        print("Inside get_all --> ",student_data)
        return Response(student_data.values(),status=status.HTTP_200_OK)

@login_required
@api_view(['GET'])
def get(request,x):
    if request.method=='GET':
        # student_id=request.data.get('id')
        try:
            student_data=Student.objects.get(id=x)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        stu_serializer=StudentSerializer(student_data)
        return Response(stu_serializer.data,status=status.HTTP_200_OK)

@login_required
@api_view(['POST'])
def delete(request):
    if request.method=='POST':
        try:
            print("Inside Delete")
            stu_id=request.data.get('id')
            student_data=Student.objects.get(id=stu_id)
            print("Student data in delete--> ",student_data)
            student_data.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        