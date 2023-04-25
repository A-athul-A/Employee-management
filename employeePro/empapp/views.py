from django.shortcuts import render
from rest_framework import generics
from .models import Emp, Department, Role
from .serializers import DepartmentSerializer, EmployeeSerializer, RoleSerialiser


# Create your views here.

class Employee(generics.ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmployeeSerializer


class Department(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Role(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerialiser
