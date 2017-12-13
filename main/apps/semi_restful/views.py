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
    return redirect("/")
# Create your views here.
