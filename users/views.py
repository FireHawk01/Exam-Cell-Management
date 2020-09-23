from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginn
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

@csrf_protect
def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username,password=password)
		if user is not None:
			loginn(request,user)
			return redirect('/')
		else:
			messages.error(request, f' Wrong credentials')
			return redirect('/login')
	return render(request, 'users/login.html')