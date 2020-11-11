from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import Profile, Elective
from exam.models import Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8

@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def f_home(request):
	return render(request, 'faculty/base.html')


@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def student_profile(request):
	if request.method == 'POST':
		roll_no = request.POST.get('rollno')
		try:
			user_obj = User.objects.get(username=roll_no.lower())
			obj = Profile.objects.get(user=user_obj)
			return render(request, 'faculty/student_profile.html',{'profile':obj})
		except:
			messages.error(request, f' Profile not found !!')
			return redirect('/faculty/studentprofile')

	return render(request, 'faculty/student_profile.html')


@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def f_backlogs(request):
	full_data = dict()
	users=User.objects.all()
	for stu in users:
		print (stu)
		back = list()
		try:
			query = Sem1.objects.get(enroll_no=stu.username)
			fields = Sem1._meta.get_fields()

			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 1',field.name)
					back.append(temp)
		except:
			print ("1")
		try:
			query = Sem2.objects.get(enroll_no=stu.username)
			fields = Sem2._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 2',field.name)
					back.append(temp)
		except:
			print ("2")
		try:
			query = Sem3.objects.get(enroll_no=stu.username)
			fields = Sem3._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 3',field.name)
					back.append(temp) 
		except:
			print ("3")
		try:
			query = Sem4.objects.get(enroll_no=stu.username)
			fields = Sem4._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 4',field.name)
					back.append(temp) 
		except:
			print ("4")
		try:
			query = Sem5.objects.get(enroll_no=stu.username)
			fields = Sem5._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 5',field.name)
					back.append(temp) 
		except:
			print ("5")
		try:
			query = Sem6.objects.get(enroll_no=stu.username)
			fields = Sem6._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 6',field.name)
					back.append(temp)
		except:
			print ("6")
		try:
			query = Sem7.objects.get(enroll_no=stu.username)
			fields = Sem7._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 7',field.name)
					back.append(temp)
		except:
			print ("7")
		try:
			query = Sem8.objects.get(enroll_no=stu.username)
			fields = Sem8._meta.get_fields()
			
			for field in fields:			
				if getattr(query,field.name) == 'F':
					temp=('Semester 8',field.name)
					back.append(temp)
		except:
			print ("8")
		if back:
			full_data[stu.username] = back 
	print (full_data)
		
	return render(request, 'faculty/f_backlogs.html',{'backlogs':full_data})


@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def f_view_elective(request):
	if request.method == 'POST':
		roll_no = request.POST.get('rollno')
		try:
			user_obj = User.objects.get(username=roll_no.lower())
			obj = Elective.objects.filter(user=user_obj,approved=True)
			return render(request, 'faculty/f_view_elective.html',{'elective':obj})
		except:
			messages.error(request, f' Not found !!')
			return redirect('/faculty/viewelective')

	return render(request, 'faculty/f_view_elective.html')


@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def approve_elective(request):
	if request.method == "POST":
		name1 = request.POST.get('idd1')
		name1 = name1.split()
		name2 = request.POST.get('idd2')
		user_obj = User.objects.get(username=name1[0])
		obj = Elective.objects.get(user=user_obj,semester=name1[1],elective=name2)
		obj.approved=True
		obj.save()

	obj = Elective.objects.filter(approved=False)
	return render(request, 'faculty/approve_elective.html',{'elective':obj})




@login_required
@user_passes_test(lambda u:u.groups.filter(name = 'faculty').exists())
def student_result(request):
	if request.method == 'POST':
		enroll_no = request.POST.get('rollno')
		semester = request.POST.get('sem')
		#semester = semester.split()[1]
		subject_res=dict()

		try:

			if semester == '1':
				res = Sem1.objects.get(enroll_no=enroll_no)	
				subject_res['fields'] = [field.name for field in Sem1._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()
				
				for field in fields:
					subject_res['marks'].append((Sem1._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '2':
				res = Sem2.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem2._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem2._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '3':
				res = Sem3.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem3._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem3._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '4':
				res = Sem4.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem4._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem4._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '5':
				res = Sem5.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem5._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem5._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '6':
				res = Sem6.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem6._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem6._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '7':
				res = Sem7.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem7._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem7._meta.get_field(field).verbose_name,str(getattr(res, field))));

			elif semester == '8':
				res = Sem8.objects.get(enroll_no=enroll_no)
				subject_res['fields'] = [field.name for field in Sem8._meta.get_fields()]

				fields = subject_res['fields']
				subject_res['marks'] = list()

				for field in fields:
					subject_res['marks'].append((Sem8._meta.get_field(field).verbose_name,str(getattr(res, field))));

		except:
			messages.error(request, f' Result not found!')
			return redirect('/faculty/studentresult')
		return render(request, 'faculty/student_result.html', subject_res)

	return render(request, 'faculty/student_result.html')