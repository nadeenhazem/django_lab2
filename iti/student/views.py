from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
# Create your views here.
def studentlist(req):
    return HttpResponse ('list student')


def studentinsert(req):
    return render(req,'insert.html')


def studentdelete(req):
    return HttpResponseRedirect ('/list')
def studentupdate(req):
    return render(req,'update.html')
def inhome(req):

    return render(req,'inhome.html')
def home(req):
    return render(req, 'home.html')