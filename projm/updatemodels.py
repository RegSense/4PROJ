import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projm.settings')
django.setup()

from django.core.management.base import BaseCommand
import pandas as pd
from django.contrib.auth.models import User
from app.models import *

def handle():
    # User
    df = pd.read_csv('../../4PROJ/Students1.csv')
    for ID,FIRST_NAME, LAST_NAME, CAMPUS, CURSUS in zip(df.id,df.first_name,df.last_name,df.campus,df.cursus):
        models = User(password=ID, username = FIRST_NAME + ' ' + LAST_NAME, first_name=FIRST_NAME, last_name=LAST_NAME, email = FIRST_NAME + "." + LAST_NAME + "@supinfo.com")
        models.save()
        data = UserData(user = models, person_id = ID,campus=CAMPUS, group=CURSUS)
        data.save()

    # Module
    #df1 = pd.read_csv('../../4PROJ/Modules1.csv')
    #for ID, MODULEID, MODULENAME, MODULEDESCRIPTION, CREDITS, CURSUS in zip(df1.id, df1.moduleId, df1.moduleName, df1.moduleDescription, df1.credits, df1.cursus):
    #    models1 = Module(id=ID, moduleId=MODULEID, moduleName=NAME, moduleDescription=MODULEDESCRIPTION, credits=CREDITS, cursus=CURSUS)
    #    models1.save()

    # Result
    df2 = pd.read_csv('../../4PROJ/Grades.csv')
    for ID,CURSUS, MODULE, ID_STUDENT, GRADE in zip(df2.id, df2.cursus, df2.module, df2.id_student, df2.grade):
        models2 = Result(id=ID, cursus=CURSUS, module=MODULE, id_student=ID_STUDENT, grade=GRADE)
        models2.save()

    # Alternance
    df3 = pd.read_csv('../../4PROJ/Alternance.csv')
    for ID,ID_STUDENT, CONTRAT, COMPANYNAME, TOPAY_STUDENT, TOPAY_COMPANY,HIRE_DAYE in zip(df3.id, df3.id_student, df3.contrat, df3.companyName, df3.topay_student, df3.topay_company, df3.hire_date):
        models3 = Alternance(id=ID, id_student=ID_STUDENT, contrat=CONTRAT, companyName=COMPANYNAME, topay_student=TOPAY_STUDENT, topay_company=TOPAY_COMPANY, hire_date=HIRE_DAYE)
        models3.save()

    # Accounting
    df4 = pd.read_csv('../../4PROJ/Accounting.csv')
    for ID,ID_STUDENT, AMOUNT_DUE, PERCENT_PAID, AMOUNT_PAID in zip(df4.id, df4.id_student, df4.amount_due, df4.percent_paid, df4.amount_paid):
        models4 = Accounting(id=ID, id_student=ID_STUDENT, amount_due=AMOUNT_DUE, percent_paid=PERCENT_PAID, amount_paid=AMOUNT_PAID)
        models4.save()

handle()