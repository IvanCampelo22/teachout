from django.http import HttpResponseRedirect, HttpResponseServerError, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import AppRegistryNotReady, FieldDoesNotExist, BadRequest
from user.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserForm
from django.urls import reverse


def create_users(request):
    try: 
        if request.method == "POST":
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/home/')

        else:
            form = UserForm()

        return render(request, "user/user_create.html", {"form": form})
    
    except AppRegistryNotReady:
        return HttpResponseServerError("The application is not ready to launch")
    
    except FieldDoesNotExist:
        return HttpResponseServerError("Sending invalid fields")
    
    except BadRequest:
        return HttpResponseServerError("Some error in server")


def get_user(request, user_id):
    try: 

        user = get_object_or_404(User, pk=user_id)
        return render(request, "user/user.html", {"user": user})
    
    except Http404:
        return HttpResponseNotFound("Usuário não encontrado")

def users_list(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "user/user_list.html", {"users": page_obj})


def update_user(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)

        if request.method == "POST":
            form = UserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/home/')
        else:
            form = UserForm(instance=user)

        return render(request, "user/user_update.html", {"form": form})
    
    except AppRegistryNotReady:
        return HttpResponseServerError("The application is not ready to launch")
    
    except FieldDoesNotExist:
        return HttpResponseServerError("Sending invalid fields")
    
    except BadRequest:
        return HttpResponseServerError("Some error in server")
    

def delete_user(request, user_id):
    try: 
        user = get_object_or_404(User, pk=user_id)
        user.is_activate = False  
        user.save() 

        messages.success(request, "Usuário desativado com sucesso.")
        return redirect(reverse('users_list'))
    except Http404:
        return HttpResponseNotFound("Usuário não encontrado")

def index(request):
    return render(request, 'index.html', {})