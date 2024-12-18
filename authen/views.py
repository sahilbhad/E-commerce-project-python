from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def register(request):
    login_nav=True
    if request.method=='POST':
     first_name=request.POST['fname']
     last_name=request.POST['lname']
     email=request.POST['email']
     username=request.POST['uname']
     password=request.POST['password']
     print(first_name,last_name,email,username,password)



     u=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
     u.save()
     return  redirect('login')
    

    context={'login_nav':login_nav}

    return render(request, 'register.html',context)



def login_(request):
       wrong_credentials=False
       login_nav=True
       
       if request.method=='POST':
          username=request.POST['uname']
          password=request.POST['password']
          # print(username,password)
         
          try:
               user=User.objects.get(username=username)
          except:
               return HttpResponse(' username doesnot exist')
          
          if user.password==password:
              if user is not None:
               login(request,user)
               return redirect('cart')
              
          else:
             wrong_credentials=True
             login_nav=False
             

       context={'wrong_credentials': wrong_credentials,'login_nav':login_nav}

       return render(request,'login.html',context)


def logout_(request):
    logout(request)
    return  redirect ('login')