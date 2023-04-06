from django.shortcuts import render,redirect
from mainapp.forms import CustomUserForm,User_detailsform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
# create your views here ;



def index(request):
    land=landingpage.objects.all()
    comment=feedback.objects.all()
    if request.method=='POST':
        if request.user.is_authenticated:
            txt=request.POST.get('txt')
            feed=feedback.objects.create(user3=request.user,comment=txt)
            feed.save()
            return redirect('/')
        else:
            messages.error(request,"login to comment")
    return render(request,'layouts/home.html',{"land":land,"comments":comment})

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request,'layouts/register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,'layouts/login.html')
    
def logout_page(request):
  
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")



def user_page(request):
    fed=feedback.objects.filter(user3=request.user)
    if request.user.is_authenticated:
        details=user_details.objects.filter(user1=request.user)
        return render(request,'layouts/user_page.html',{"details":details,'feedback':fed})
    else:
        return redirect("/")
   
def update_details(request,id):
    if request.user.is_authenticated:
        saved=user_details.objects.filter(id=id)
        if request.method=='POST' and request.FILES:
            about=request.POST.get('about')
            img=request.FILES['image']
            saved=user_details.objects.get(id=id)
            saved.about=about
            saved.images=img
            saved.user1=request.user
            saved.save()
            messages.success(request,"User details  succesfully updated.")
            return redirect("user_page")
    return render(request,'layouts/User_update.html',{'saved':saved})   

def add_user_details(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=User_detailsform(data=request.POST,files=request.FILES)
            if form.is_valid():
                about=form.cleaned_data['about']
                image=form.cleaned_data['images']
                item=user_details.objects.create(user1=request.user,about=about,images=image)
                item.save()
                messages.success(request,"User details added succesfully.")
                return redirect("user_page")
        else:
            form=User_detailsform()
            messages.error(request,"Encountered a error.")
    return render(request,'layouts/add_user_details.html',{'forms':form})

def delete_user_details(request,id):
    details=user_details.objects.filter(id=id,user1=request.user)
    details.delete()
    return redirect('user_page')

def deletecomment(request,id):
    details=feedback.objects.filter(id=id,user3=request.user)
    if details:
        details.delete()
        messages.success(request,"comment deleted successfully ")
    else:
        messages.error(request,'Something went wrong Please try again after sometimes.')
    return redirect('user_page')
def editcomment(request,id):
    if request.user.is_authenticated:
        details=feedback.objects.filter(id=id)
        if request.method=='POST':
            txt=request.POST.get('txt')
            details=feedback.objects.get(id=id)
            details.user3=request.user
            details.comment=txt
            details.save()
            messages.success(request,"Your comment succesfully updated.")
            return redirect("user_page")
    return render(request,'layouts/editcomment.html',{'feed':details})