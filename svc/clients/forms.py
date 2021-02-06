from django import forms
from .models import User, JobPost


class CustomClientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'number', 'zipcode', 'usertype')
        widgets = {
            'usertype': forms.RadioSelect()
        }  

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        # fields = '__all__'
        exclude = ('client',)
