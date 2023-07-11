from django.shortcuts import render,redirect
from accounts.models import Account
from django.contrib.auth import authenticate,login ,logout

# Create your views here.
def signinPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Account.objects.get(email=email)
            if user:
                auth_user = authenticate(request,email=email,password=password)
                if auth_user:
                    login(request,user)
                    return redirect("home")
                else:
                    print("pass salah")
                    return redirect("accounts:signin")
        except:
            context={
            'title':'Login | Page',
            'info':'email salah'
            }
            return render(request,'accounts/signin.html',context)
            
    
    context={
        'title':'Login | Page',
    }
    return render(request,'accounts/signin.html',context)

def logoutPage(request):
    logout(request=request)
    return redirect("accounts:signin")