# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

def index(request):
    all_users = User.objects.all()
    context = {
        "users" : all_users
    }
    return render(request, 'index.html', context)

def add(request):
    return render(request, "add.html")
def add_user(request):
    if request.method == "POST":
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        email = request.POST["email"]
        User.objects.create(first_name = first, last_name=last, email= email)
        return redirect("/")
    else:
        return redirect('/add')
    return redirect("/")

def edit(request, user_id):
    request.session["user_id"] = user_id
    
    
    return render(request, "edit.html")
def edit_user(request):
    
    if request.method == "POST":
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        email = request.POST["email"]
        User.objects.filter(id = request.session["user_id"]).update(first_name = first, last_name=last, email= email)
        return redirect("/")
    else:
        return redirect('/add')
    return redirect("/")

def delete(request, user_id):
    print user_id
    User.objects.filter(id = user_id).delete()
    return redirect("/")

# Create your views here.
