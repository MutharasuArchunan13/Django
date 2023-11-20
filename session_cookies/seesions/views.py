from django.shortcuts import render

# Create your views here.
def count_sessions(request):
    count = request.session.get('count',0)
    total_count = int (count) + 1
    request.session['count'] = total_count
    return render(request,'cookies/cookie.html',{'counts':total_count})