from django.shortcuts import render
import datetime
# Create your views here.
def html_file_rendering(request):
    date = datetime.datetime.now()
    date_dict ={'datetim':date}
    return render(request,'temp_projects/temp.html',context=date_dict)
