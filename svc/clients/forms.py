from django import forms
from accounts.models import TopicList, TopicDetailList, AssetsDetailList, TopicSubCats

class JobPostForm(forms.ModelForm):
    class Meta:
        model = TopicList
        fields = '__all__'  # ('TopicName',)
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'SMSText', 'WhatsAppText', 'CloseBy_id', 'ForceCloseCategory', 'City', 'Category', 'SubCategory', 'UpdatedBy', 'AddedBy', 'CloseBy', 'IsClose', 'IsActive')

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = TopicList
        fields = '__all__'
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'CloseBy_id', 'ForceCloseCategory', 'AddedBy', 'UpdatedBy', 'City', 'Category', 'SubCategory', 'CloseBy', 'IsActive')


class AssetsForm(forms.ModelForm):
    class Meta:
        model = AssetsDetailList
        fields = ['FileName']



class TopicSubCatsForm(forms.ModelForm):
    class Meta:
        model = TopicSubCats
        fields = '__all__'
