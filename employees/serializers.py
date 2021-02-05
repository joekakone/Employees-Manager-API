from rest_framework import serializers

from employees.models import Department, Employee, DepartmentManager

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
	class Meta:
		model = DepartmentManager
		fields = '__all__'
