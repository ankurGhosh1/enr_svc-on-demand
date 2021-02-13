from django import forms
from accounts.models import TopicList, TopicDetailList 

class JobPostForm(forms.ModelForm):
    class Meta:
        model = TopicList
        fields = '__all__'  # ('TopicName',)
        exclude = ('UpdatedDate', 'CloseDate', 'ForceCloseReason', 'SMSText', 'WhatsAppText', 'CloseBy_id', 'ForceCloseCategory', 'UpdatedBy', 'CloseBy', 'IsClose', 'IsActive')

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = TopicList
        fields = '__all__'