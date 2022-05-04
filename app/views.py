from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
def home(request):
    return render(request,template_name='home.html')

def login_view(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        try:
            user=User.objects.all().get(username=username)
        except:
            messages.error(request,"No User exists with this Username.")
            return render(request,'login.html')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if 'next' in data:
                return redirect(data.get('next'))
            return redirect("/home/")
        else:
            messages.error(request,"Invalid Password.") 
    return render(request,'login.html')

def register(request):
    context={}
    if request.method=="POST":
        data=request.POST
        firstname=data.get('firstname')
        lastname=data.get('lastname')
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        repassword=data.get('repassword')
         
        try:
            user=User.objects.all().get(email=email)
            messages.error(request,"User already exit with this email")
            return render(request,'register.html',context=context)
        except:
            try:
                user=User.objects.all().get(username=username)
                messages.error(request,"User already exit with this email")
                return render(request,'register.html',context=context)
            except:
                if(password!=repassword):
                    messages.error(request,"Password not matched.")
                    return render(request,'register.html',context=context)
                else:
                    user=User(username=username,
                            first_name=firstname,
                            last_name=lastname,
                            email=email,
                            password=password)    
                    user.save()
                    return redirect("/login/")    
    return render(request,'register.html',context=context)

def logout_view(request):
    logout(request)
    print(request.user.username)
    return redirect('/home/')

def search(request):
    context={}
    if request.method=="POST":
        data=request.POST
        source=data.get("source")
        dest=data.get("destination")
        buses=Bus.objects.filter(dest__istartswith=dest,source__istartswith=source)
        context['buses']=buses
    return render(request,"search.html",context)

def book(request,id):
    bus=Bus.objects.all().get(id=id)
    if request.method=="POST":
        data=request.POST
        tickets=int(data.get("tickets"))
        user=request.user
        cost=tickets*bus.price
        booking=Booking(tickets=tickets,user=user,bus=bus,cost=cost)
        booking.save()
        messages.info(request,"Ticket is booked")
    return render(request,"book.html",{"bus":bus})

def bookings(request):
    context={}
    user=request.user
    bookings=Booking.objects.filter(user=user,status="BOOKED")
    context['bookings']=bookings
    return render(request,'bookings.html',context)

def cancel_bookings(request,id):
    object=get_object_or_404(Booking,id=id)
    object.status="CANCEL"
    object.save()
    return redirect('/bookings/')

def caneceld_booking(request):
    context={}
    user=request.user
    bookings=Booking.objects.filter(user=user,status="CANCEL")
    context['bookings']=bookings
    return render(request,'cancel.html',context)







