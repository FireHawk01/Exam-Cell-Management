from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name= 'home'),
        path('result/', views.result, name= 'result'),
        path('result/show/', views.show, name= 'showresult'),
        path('announcements/', views.announcements, name= 'announcements'),
        path('<path:path>/', views.download, name= 'announcements'),

]
