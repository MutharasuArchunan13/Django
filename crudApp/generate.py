import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudApp.settings')

import django
django.setup()

from crudoperations.models import student
from faker import Faker
from random import randint

faker = Faker()  # Corrected object name

def generate_fake(n):
    for i in range(n):
        fname = faker.name()  # Corrected object name
        froll = randint(1, 180)
        fid = randint(180, 300)
        record, created = student.objects.get_or_create(name=fname, roll=froll, sid=fid)
        record.save()

generate_fake(40)
