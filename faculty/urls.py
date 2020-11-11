from django.urls import path
from . import views

urlpatterns = [
			path('home/', views.f_home ,name='f_home'),
			path('studentprofile/', views.student_profile ,name='student_profile'),
			path('backlogs/', views.f_backlogs ,name='f_backlogs'),
			path('viewelective/', views.f_view_elective ,name='f_view_elective'),
			path('approveelective/', views.approve_elective ,name='approve_elective'),
			path('studentresult/', views.student_result ,name='student_result'),

]