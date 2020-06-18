from django.db import models


class Designation(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=250)
    emp_code = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
