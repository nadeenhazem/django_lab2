from django.shortcuts import render
from django.contrib.auth.models import User
from myuser.models import myuser
from django.contrib.auth import authenticate ,login  as authlogin ,logout  as authlogout
def login(req):
    #req.session.clear()
    if (req.session.get('username') is None):
        if (req.method == 'GET'):
            return render(req, 'login.html')
        else:
            myuserobject=myuser.objects.filter(username=req.POST['username'],password=req.POST['password'])
            authuser=authenticate(username=req.POST['username'],password=req.POST['password'])
            if (len(myuserobject) > 0 and authuser is not None):
                req.session['username'] = myuserobject[0].username
                authlogin(req,authuser)
                return render(req, 'home.html')
            else:
                context = {}
                context['Erorr'] = 'invalid user.'

                return render(req, 'login.html',context)
    else:
        return render(req, 'inhome.html')

def register(req):
    if (req.method=='GET'):
        return render(req,'register.html')
    else:
        print(req.POST)
        use=myuser(username=req.POST['username'])
        use.email=req.POST['email']
        use.password=req.POST['password']

        use.save()

        User.objects.create_user(username=req.POST['username'], email=req.POST['email'],password=req.POST['password'],is_superuser=True,is_staff=True)
        return render(req, 'login.html')

def logout(req):
    if (req.session.get('username') is None and req.t.user.is_authenticated()):
        req.session.clear()
        authlogout(req, req.user)
    return render(req, 'inhome.html')

def home(req):
    if (req.session.get('username') is None and req.t.user.is_authenticated()):
        return render(req, 'inhome.html')
    else:
        return render(req, 'login.html')
