from django.db import models
from django.contrib.auth.models import User

# Classe UserData
class UserData(models.Model):
    user = models.ForeignKey(User, primary_key=True, on_delete = models.CASCADE)
    campus = models.CharField(max_length=30, null = False)
    person_id = models.CharField(max_length=40, null = False)
    group = models.CharField(max_length=30, null = False, default = '')

    def __str__(self):
        return self.person_id

# Classe Module
class Module(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    moduleId = models.CharField(max_length=10)
    moduleName = models.CharField(max_length=200)
    moduleDescription = models.CharField(max_length=500)
    credits = models.IntegerField()
    cursus = models.CharField(max_length=10)

    def __str__(self):
        return self.moduleId

# Classe Result
class Result(models.Model):
    id = models.BigAutoField(primary_key=True)
    cursus = models.CharField(max_length=10)
    module = models.CharField(max_length=10)
    id_student = models.CharField(max_length=40, null = False)
    grade = models.FloatField()

    def __str__(self):
        return self.id_student


# Classe Alternance
class Alternance(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_student = models.CharField(max_length=40, null = False)
    contrat = models.CharField(max_length=10, null = False)
    companyName = models.CharField(max_length=30, null = False)
    topay_student = models.FloatField()
    topay_company = models.FloatField()
    hire_date = models.CharField(max_length=20)

    def __str__(self):
        return self.id_student

# Classe Accounting
class Accounting(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_student = models.CharField(max_length=40, null = False)
    amount_due = models.FloatField()
    percent_paid = models.FloatField()
    amount_paid = models.FloatField()

    def __str__(self):
        return self.id_student