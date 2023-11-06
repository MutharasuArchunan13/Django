from django.shortcuts import render
import random
from django.http import HttpResponse
import random
# Create your views here.
def ran_num(request):
    lis=[]
    for i in range(100):
        lis.append(i)
    message='<h1>This is our random number game:{}'.format(random.choice(lis))
    return HttpResponse(message)
