from django.urls import path
from employees.apiviews import DepartmentList, EmployeeList, ManagerList


urlpatterns = [
	# Departments
	path("departments/", DepartmentList.as_view(), name="departments_list"),

	# Employees
	path("employees/", EmployeeList.as_view(), name="employees_list"),

	# Managers
    path("managers/", ManagerList.as_view(), name="managers_list"),
]
