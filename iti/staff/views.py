from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect ,JsonResponse
# Create your views here.
def stafflist(req):
    return HttpResponse ('list staff')


def staffinsert(req):

    return JsonResponse ({'name':'insert'})


def staffdelete(req):
    return HttpResponseRedirect ('/listt')
def staffupdate(req):
    return JsonResponse ({'name':'update'})
