from django.contrib import admin

# Register your models here.
from employees.models import Department, Employee, DepartmentEmployee, DepartmentManager, Salary, Title


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(DepartmentEmployee)
admin.site.register(DepartmentManager)
admin.site.register(Salary)
admin.site.register(Title)
