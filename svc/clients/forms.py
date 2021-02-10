from django import forms
from accounts.models import UserList #, JobPost


class CustomClientUserForm(forms.ModelForm):
    class Meta:
        model = UserList
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'usertype')
        widgets = {
            'usertype': forms.RadioSelect()
        }  

# class JobPostForm(forms.ModelForm):
#     class Meta:
#         model = JobPost
#         # fields = '__all__'
#         exclude = ('client',)