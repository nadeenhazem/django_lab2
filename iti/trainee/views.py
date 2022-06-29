from django.shortcuts import render
from myuser.models import myuser
from django.http import HttpResponseRedirect

# Create your views here.
def listuser(req):
    allUsers=myuser.objects.all()
    context={}
    context['users']=allUsers
    return render(req,'usersList.html',context)
def Update(req,id):
    if(req.session.get('username') is not None):

        context = {}
        if (req.method == "GET"):
            context['users']=myuser.objects.get(id=id)
            return render(req, 'Update.html', context)
        else:
            myuser.objects.filter(id=id).update(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'])
            return HttpResponseRedirect('/User')
    else:
        return HttpResponseRedirect('/login')

def Delete(req,id):
    if(req.session.get('username') is not None):
        deleteuser= myuser.objects.filter(id=id).delete()
        return HttpResponseRedirect('/User')

    else:
        return HttpResponseRedirect('/login')



