from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from todo_list import models
from todo_list.models import TODOO

from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

User = get_user_model()

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('todo:login')  # Redirect to login after logout

@login_required
def delete_task(request, srno):
    task = get_object_or_404(TODOO, srno=srno, user=request.user)
    task.delete()
    return redirect('todo:todo')

@login_required
def edit_task(request, srno):
    task = get_object_or_404(TODOO, srno=srno, user=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title', '').strip()
        if new_title:
            task.title = new_title
            task.save()
            return redirect('todo:todo')
        else:
            messages.error(request, "Task title cannot be empty!")

    return render(request, 'edit_task.html', {'task': task})




def home(request):
    return HttpResponse("Hello, World!")

def signup(request):
    if request.method== 'POST':
        fnm = request.POST.get('fnm')
        emailid= request.POST.get('email')
        pwd=request.POST.get('pwd')
        if User.objects.filter(username=fnm).exists():
            messages.error(request, "Username already taken.")
            return redirect('todo:signup')
        print(fnm, emailid,pwd)
        my_user= User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        messages.success(request, "Account created successfully!")
        return redirect('todo:login')
    return render(request,"signup.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect('todo:todo')

    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        userr =authenticate(request, username=fnm, password=pwd)
        if userr is not None :
            django_login(request, userr)
            return redirect('todo:todo')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

@login_required(login_url='todo:login')
def todo(request):
    if request.method== 'POST':
        title = request.POST.get('title').strip()
        print(title)
        if title:
            obj=models.TODOO(title=title, user=request.user)
            obj.save()
            messages.success(request, "Task added successfully!")
        return redirect('todo:todo')
    res=models.TODOO.objects.filter(user=request.user).order_by('-date') # filtering todo for the connected user
    return render(request,'todo.html',{'res':res})
