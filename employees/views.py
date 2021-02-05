from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from employees.models import Department, Employee, DepartmentManager


def departments_list(request):
    MAX_OBJECTS = 20
    departments = Department.objects.all()[:MAX_OBJECTS]
    data = {"results": list(departments.values())}

    return JsonResponse(data)

def departments_details(request, pk):
    department = get_object_or_404(Department, pk=pk)
    # data = {"results": {
    #     "question": department.question,
    #     "created_by": department.created_by.username,
    #     "pub_date": department.pub_date
    # }}
    data = {"results": dict(department)}

    return JsonResponse(data)

def employees_list(request):
    MAX_OBJECTS = 20
    employees = Employee.objects.all()[:MAX_OBJECTS]
    data = {"results": list(employees.values())}

    return JsonResponse(data)

def employees_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = {"results": dict(employee)}

    return JsonResponse(data)

def managers_list(request):
    MAX_OBJECTS = 20
    managers = DepartmentManager.objects.all()[:MAX_OBJECTS]
    data = {"results": list(managers.values())}

    return JsonResponse(data)

def managers_details(request, pk):
    manager = get_object_or_404(DepartmentManager, pk=pk)
    data = {"results": dict(manager)}

    return JsonResponse(data)
