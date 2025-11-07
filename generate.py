import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjangoProject.settings')

import django
django.setup()

from faker import Faker
from random import randint
from CRUDApp.models import Employee

fake=Faker()
def generatefakedata():
    f_id=randint(10000,99999)
    f_name=fake.name()
    f_email=fake.email()
    f_ph=randint(6000000000, 9999999999)
    f_city=fake.city()
    Employee.objects.get_or_create(empid=f_id,
                                   name=f_name,
                                   email=f_email,
                                   phonenumber=f_ph,
                                   city=f_city)

for i in range(0,10,1):
    generatefakedata()
