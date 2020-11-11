from django.urls import path
from . import views

urlpatterns = [
			path('login/', views.login ,name='login'),
			path('profile/', views.showprofile ,name='showprofile'),
			path('profile/update/', views.updateprofile ,name='updateprofile'),
			path('elective/', views.elective, name='elective'),
			path('elective/sem/', views.select_elective_sem, name='select_elective_sem'),
			path('elective/sem/select/', views.select_elective, name='select_elective'),
			path('elective/view/', views.view_elective, name='view_elective'),
			path('backlogs/',views.backlogs, name='backlogs'),
]