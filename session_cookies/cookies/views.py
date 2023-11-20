from django.shortcuts import render

# Create your views here.
"""COOKIES   have small amount of data so it store all datas are string format"""
def cookies_count(request):
    count = request.COOKIES.get('count',0)
    total_count = int (count) + 1
    response = render(request,'cookies/cookie.html',{'count':total_count})
    response.set_cookie('count',total_count)
    return response