from rest_framework import generics

from employees.models import Department, Employee, DepartmentManager
from employees.serializers import DepartmentSerializer, EmployeeSerializer, ManagerSerializer


class DepartmentList(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer

class EmployeeList(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class ManagerList(generics.ListCreateAPIView):
	queryset = DepartmentManager.objects.all()
	serializer_class = ManagerSerializer
