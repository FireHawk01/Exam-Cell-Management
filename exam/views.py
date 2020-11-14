from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8
from django.db import models
from django.contrib import messages
import io, os
from django.http import FileResponse, HttpResponse, Http404
from reportlab.pdfgen import canvas
from faculty.models import Announcements
from django.conf import settings


def home(request):
	if request.user.groups.filter(name = 'faculty').exists():
		return redirect('/faculty/home')
	return render(request, 'exam/base.html')

@login_required
def result(request):
	subject_res=dict()
	subject_res['semesters'] = ['1','2','3','4','5','6','7','8']
	return render(request,"exam/result.html",subject_res)

@login_required
def show(request):
	if request.method == 'POST':
		#sem1 = Sem1(enroll_no='lit2018070',SGPI='3.4')
		#Sem1.objects.get(enroll_no='lit2018070').delete()
		enroll_no = request.user.username
		subject_res=dict()
		semester = request.POST.get('semester')

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
			elif semester == '':
				messages.error(request, f' Please enter the semester!')
				return redirect('result')

		except:
			messages.error(request, f' Result not found!')
			return redirect('result')


		
		return render(request,"exam/showresult.html",subject_res)
	else:
		return redirect('result')



def announcements(request):
	query = Announcements.objects.all()
	return render(request,"exam/announcements.html",{"announcements":query})



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print("*")
    print (file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
