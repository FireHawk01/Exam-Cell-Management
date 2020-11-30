from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginn
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfile
from .models import Profile, Elective
from exam.models import Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8

@csrf_protect
def login(request):
	if request.method == "POST":
		username = request.POST.get('username').split('@')[0].lower()
		password = request.POST.get('password')
		user = authenticate(request, username=username,password=password)
		if user is not None:
			loginn(request,user)
			if user.groups.filter(name = 'faculty').exists():
				return redirect('/faculty/home')
			else:
				return redirect('/')
		else:
			messages.error(request, f' Wrong credentials')
			return redirect('/users/login')
	return render(request, 'users/login.html')

@login_required
def showprofile(request):
	try:
		obj = Profile.objects.get(user=request.user)			
	except:
		obj = Profile(user=request.user)
		obj.save()
	return render (request, 'users/showprofile.html', {'context':obj})


@login_required
def updateprofile(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = UpdateProfile(request.POST)
        # check whether it's valid:
		if form.is_valid():
			obj1 = Profile.objects.get(user=request.user)
			obj2 = User.objects.get(username=request.user.username)
			obj2.first_name = form.cleaned_data['f_name']
			obj2.last_name = form.cleaned_data['l_name']
			obj1.contact=form.cleaned_data['contact']
			obj1.address=form.cleaned_data['address']
			obj1.save()
			obj2.save()
		return redirect('/users/profile/')

    # if a GET (or any other method) we'll create a blank form
	else:
		try:
			obj = Profile.objects.get(user=request.user)			
		except:
			obj = Profile(user=request.user)
			obj.save()
		obj = Profile.objects.get(user=request.user)
		updateform = UpdateProfile(initial={'enroll_no': request.user.username.upper(),'f_name':request.user.first_name,'l_name':request.user.last_name,'contact':obj.contact,'address':obj.address})
		context ={
		'updateform':updateform,
		}
		return render (request, 'users/updateprofile.html', context)

@login_required
def elective(request):
	return render (request, 'users/elective.html')

@login_required
def select_elective_sem(request):
	subject_res=dict()
	subject_res['semesters'] = ['6','7']
	return render(request,"users/select_elective_sem.html",subject_res)




@login_required
def select_elective(request):
	if request.method == "POST" and not request.POST.get('semester') :
		ele_1 = request.POST.get('Elective 1')
		ele_2 = request.POST.get('Elective 2')
		ele_3 = request.POST.get('Elective 3')

		if ele_1 != ele_2 and ele_2!= ele_3 and ele_3!=ele_1:
			#print(request.POST.get('Elective 2'))
			sem = 6
			if ele_3 is not None:
				sem = 7
			user = request.user


			obj1 = Elective(user=user,elective=ele_1,semester=sem)
			obj1.save()
			obj2 = Elective(user=user,elective=ele_2,semester=sem)
			obj2.save()
			if ele_3 is not None:
				obj3 = Elective(user=user,elective=ele_3,semester=sem)
				obj3.save()
			return redirect('/users/elective/view/')
		else:
			messages.error(request, f' All electives should be different!')
			return redirect('/users/elective/sem/select/')

	#elif request.method == "POST" and request.POST.get('semester') :

	else:
		subject_res=dict()	
		semester = request.POST.get('semester')
		if semester is None:
			return redirect('/users/elective/sem/')
		#print(Elective.objects.filter(user=request.user,semester=semester))
		if Elective.objects.filter(user=request.user,semester=semester):
			messages.error(request, f' Elective already chosen for this semester!')
			return redirect('/users/elective/sem/')

		if semester == '7':
			subject_res['semester'] = '7'
		subject_res['electives'] = ['Optimization Techniques','Machine Learning - Tools And Techniques','Wireless Sensor Networks','Architecture of Software Systems','Advanced Graphics and Animation','Information Retrieval Systems','Cryptography and Information Security','Modeling, Design and Analysis of Embedded System','Data Compression']
		return render(request,"users/select_elective.html",subject_res)


@login_required
def view_elective(request):
	obj = Elective.objects.filter(user=request.user)

	return render (request, 'users/view_elective.html',{'electives':obj})


@login_required
def backlogs(request):
	back = list()
	try:
		query = Sem1.objects.get(enroll_no=request.user.username)
		fields = Sem1._meta.get_fields()

		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 1',field.name)
				back.append(temp)
	except:
		print ("1")
	try:
		query = Sem2.objects.get(enroll_no=request.user.username)
		fields = Sem2._meta.get_fields()
		back['Semester 2'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 2',field.name)
				back.append(temp)
	except:
		print ("2")
	try:
		query = Sem3.objects.get(enroll_no=request.user.username)
		fields = Sem3._meta.get_fields()
		back['Semester 3'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 3',field.name)
				back.append(temp) 
	except:
		print ("3")
	try:
		query = Sem4.objects.get(enroll_no=request.user.username)
		fields = Sem4._meta.get_fields()
		back['Semester 4'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 4',field.name)
				back.append(temp) 
	except:
		print ("4")
	try:
		query = Sem5.objects.get(enroll_no=request.user.username)
		fields = Sem5._meta.get_fields()
		back['Semester 5'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 5',field.name)
				back.append(temp) 
	except:
		print ("5")
	try:
		query = Sem6.objects.get(enroll_no=request.user.username)
		fields = Sem6._meta.get_fields()
		back['Semester 6'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 6',field.name)
				back.append(temp)
	except:
		print ("6")
	try:
		query = Sem7.objects.get(enroll_no=request.user.username)
		fields = Sem7._meta.get_fields()
		back['Semester 7'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 7',field.name)
				back.append(temp)
	except:
		print ("7")
	try:
		query = Sem8.objects.get(enroll_no=request.user.username)
		fields = Sem8._meta.get_fields()
		back['Semester 8'] = list()
		for field in fields:			
			if getattr(query,field.name) == 'F':
				temp=('Semester 8',field.name)
				back.append(temp)
	except:
		print ("8")
	return render(request, 'users/backlogs.html',{'backlogs':back})

