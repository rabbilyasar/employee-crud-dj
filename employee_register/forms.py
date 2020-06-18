from django import forms
from employee_register.models import *


class EmployeeForm(forms.ModelForm):
    # fullname = forms.CharField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['designation'].empty_label = "Select"
        self.fields['emp_code'].required = False
