from django.http import HttpResponse
from django.shortcuts import render, redirect

from vehicle_register.forms import vehicle_form
from vehicle_register.models import Vehicle
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superadmin:
                login(request, user)
                return redirect('superadmin')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('user')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


# def superadmin(request):
#     return render(request,'superadmin.html')


def admin(request):
    veh = Vehicle.objects.all()
    context = {
        'veh' : veh
    }
    print(context)
    return render(request,'admin.html',context)


def user(request):
    veh = Vehicle.objects.all()
    context = {
        'veh' : veh
    }
    return render(request,'user.html',context)

def superadmin(request):
    veh = Vehicle.objects.all()
    context = {
        'veh' : veh
    }
    print(context)
    return render(request,'superadmin.html',context)


def superadmin_add(request):
        if request.method == 'POST':
            vehicle_number = request.POST['vehicle_number']
            vehicle_type = request.POST['vehicle_type']
            vehicle_model = request.POST['vehicle_model']
            vehicle_description = request.POST['vehicle_description']
            new_veh = Vehicle(vehicle_number=vehicle_number,vehicle_type=vehicle_type,vehicle_model=vehicle_model,vehicle_description=vehicle_description)
            new_veh.save()
            return render(request,'add_success.html')
        elif request.method=='GET':
            return render(request,'add.html')
        else:
            return HttpResponse("An Exception occured")
def  superadmin_update(request,veh_id=0):
    veh = Vehicle.object.get(id=veh_id)
    f=vehicle_form(request.POST or None,instance=Vehicle)
    return render(request,'update.html',{'Vehicle':Vehicle})
def superadmin_delete(request,veh_id=0):
    if veh_id:
        try:
            veh_to_be_removed = Vehicle.objects.get(id=veh_id)
            veh_to_be_removed.delete()
            return render(request,"del_success.html")
        except:
            return HttpResponse("An Error occured.")
    veh = Vehicle.objects.all()
    context = {
        'veh': veh
    }
    return render(request,'delete.html',context)
