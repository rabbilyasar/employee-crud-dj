from django.shortcuts import render, redirect

from employee_register.views import *
from employee_register.forms import *
from employee_register.models import *


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(id=pk)
            form = EmployeeForm(instance=employee)

        context = {'form': form}
        return render(request, 'employee_register/employee_form.html', context)
    else:
        if pk == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(id=pk)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_register:employee_list')


def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('employee_register:employee_list')
