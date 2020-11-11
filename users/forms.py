from django import forms
from django.contrib.auth.models import User


class UpdateProfile(forms.Form):
    enroll_no = forms.CharField(label='Your Enrollment Number', max_length=100,disabled= True,required=False)
    f_name = forms.CharField(label='First Name', max_length=100,required=False)
    l_name = forms.CharField(label='Last Name', max_length=100,required=False)
    contact = forms.IntegerField(label='Contact Number',max_value = 9999999999,required=False)
    address = forms.CharField(label='Address', max_length=100,required=False)