from django.urls import path ,include
from student.views import *
from staff.views import *
from reports.views import *
from iti.views import *
from .views import *


urlpatterns = [
    path('',listuser),
    path('Update/<id>/',Update,name='updateuser'),
    path('Delete/<id>/',Delete,name='deleteuser'),

   ]