from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect ,JsonResponse
# Create your views here.
def liststudent(req):
    return HttpResponse ('studentlist ')


def liststaff(req):

    return HttpResponse ('stafflist ')

def mainreport(req):
    response = HttpResponse()
    response.write('<a href="https://www.google.com/">GooGLe'
                   '</a>')
    return response





