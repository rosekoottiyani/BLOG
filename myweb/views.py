from django.shortcuts import render
from .forms import reg
from .models import register,blog
# Create your views here.
def index(request):
  return render(request,'index.html')
def regist(request):
  if request.method=="POST":
    #form=reg(request.POST)
    #if form.is_valid():
     if((request.POST.get('usr'))and(request.POST.get('pwd'))and(request.POST.get('name'))and (request.POST.get('mail'))and(request.POST.get('mob'))):
       obj=register()
       obj.username=request.POST.get('usr')
       obj.password=request.POST.get('pwd')
       obj.name=request.POST.get('name')
       obj.email=request.POST.get('mail')
       obj.mobile=request.POST.get('mob')
       obj.question=request.POST.get('question')
       obj.answer=request.POST.get('answer')
       obj.save()
       return render(request,'login.html')
     #else:
       #return render(request,'register.html')

  else:
    #form=reg()
    return render(request,'register.html')

def login(request):
  if request.method=='POST':
     
        uname=request.POST.get('usr','')
        passwd=request.POST.get('pwd','')
        try:
         obj=register.objects.get(username=uname)
       
         if(obj is not None and obj.password==passwd):
           request.session["username"]=uname
           return render(request,'user.html')
         else:
           return render(request,'login.html')
        except register.DoesNotExist:
            return render(request,'login.html')
  else:
       return render(request,'login.html')


def cblog(request):
    if (request.method == "POST"):
        if ((request.POST.get('bname')) and (request.POST.get('author')) and (request.POST.get('blog'))):
            obj = blog()
            obj.username = request.session['username']
            obj.bname = request.POST.get('bname')
            obj.author = request.POST.get('author')
            obj.blog = request.POST.get('blog')
            obj.save()
            return render(request, 'vblog.html')

    else:
        return render(request, 'blog.html')




def reset(request):
    if request.method=='POST':
      uname = request.POST.get('usr')
      passwd=request.POST.get('pwd')
      try:
          if register.objects.get(username=uname,password=passwd):
            newpwd=request.POST.get('newpass')
            register.objects.filter(username=uname).update(password=newpwd)
            return render(request,'index.html')
      except register.DoesNotExist:
            return render(request,'reset.html')
    else:
        return render(request,'reset.html')



def logout(request):
    try:
        del request.session["username"]
    except:
        pass
    return render(request, 'login.html')
    







