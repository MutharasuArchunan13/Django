from django.urls import path
from crudoperations import views
urlpatterns = [
    path('check/',views.studtent_retrive,name='crudoperations'),
    path('add/',views.add_student,name='add_student'),
    path('delete/<int:id>/',views.delete_student,name='delete'),
    path('update/<int:id>/',views.update_student,name='update'),

]
