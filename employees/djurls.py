from django.urls import path
from employees.views import departments_list, departments_details, employees_list, employees_details, managers_list, managers_details


urlpatterns = [
	path("departments/", departments_list, name="departments_list"),
    path("departments/<int:pk>/", departments_details, name="departments_details"),

	path("employees/", employees_list, name="employees_list"),
    path("employees/<int:pk>/", employees_details, name="employees_details"),

    path("managers/", managers_list, name="managers_list"),
    path("managers/<int:pk>/", managers_details, name="managers_details"),
]
