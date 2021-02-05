from django.db import models

# Create your models here.

class Department(models.Model):
	dep_no = models.IntegerField()
	dep_name = models.CharField(max_length=40)

	def __str__(self):
		return self.dep_name


class Employee(models.Model):
	GENDERS = ( 
		('F', 'Female'), 
		('M', 'Male'),  
	)
	emp_no = models.IntegerField()
	birth_date = models.DateField()
	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=16)
	gender = models.CharField(max_length=1, choices=GENDERS)
	hire_date = models.DateField()
	
	def __str__(self):
		return self.first_name + " " + self.last_name


class DepartmentEmployee(models.Model):
	emp_no = models.ForeignKey('Employee', on_delete=models.CASCADE)
	dep_no = models.ForeignKey('Department', on_delete=models.CASCADE)
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return str(self.dep_no) + " : " + str(self.emp_no)


class DepartmentManager(models.Model):
	emp_no = models.ForeignKey('Employee', on_delete=models.CASCADE)
	dep_no = models.ForeignKey('Department', on_delete=models.CASCADE)
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return str(self.dep_no) + " : " + str(self.emp_no)


class Salary(models.Model):
	emp_no = models.ForeignKey('Employee', on_delete=models.CASCADE)
	salary = models.IntegerField()
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return str(self.emp_no) + " : " + str(self.salary)


class Title(models.Model):
	emp_no = models.ForeignKey('Employee', on_delete=models.CASCADE)
	tilte = models.CharField(max_length=50)
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return self.tilte
