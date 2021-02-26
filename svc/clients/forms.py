from django import forms
from accounts.models import TopicList, TopicDetailList, AssetsDetailList, ReviewList, CategoryList, SubCategoryList, CountryList, UserList
from accounts.models import TopicList, TopicDetailList, AssetsDetailList, TopicSubCats

class JobPostForm(forms.ModelForm):
    class Meta:
        model = TopicList
        fields = '__all__'  # ('TopicName',)
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'SMSText', 'WhatsAppText', 'CloseBy_id', 'Category','City', 'ForceCloseCategory', 'UpdatedBy', 'AddedBy', 'CloseBy', 'IsClose', 'IsActive', 'IsNotification')

    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        self.fields['TopicName'].label = "Topic Name"

class JobUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobUpdateForm, self).__init__(*args, **kwargs)
        self.fields['TopicName'].label = "Topic Name"
        self.fields['SMSText'].label = "Text"
        self.fields['WhatsAppText'].label = "WhatsApp Text"

    class Meta:
        model = TopicList
        fields = '__all__'
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'CloseBy_id', 'ForceCloseCategory', 'AddedBy', 'UpdatedBy', 'City', 'Category', 'SubCategory', 'CloseBy', 'IsActive')


class AssetsForm(forms.ModelForm):
    class Meta:
        model = AssetsDetailList
        fields = ['FileName']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewList
        fields = '__all__'
        exclude = ('ReviewDate', 'SubCategory', 'Category', 'City', 'ToUser', 'FromUser', 'AssetsDetail', 'User', 'AddedBy', 'AddedDate', 'UpdatedBy', 'UpdatedDate', 'IsActive', 'IsAdminApproved')

class TopicSubCatsForm(forms.ModelForm):
    class Meta:
        model = TopicSubCats
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryList
        fields = '__all__'
        exclude = ('UpdatedBy', 'IsActive', 'AddedDate', 'AddedBy', 'UpdatedDate')


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategoryList
        fields = '__all__'
        exclude = ('UpdatedBy', 'IsActive', 'AddedDate', 'AddedBy', 'UpdatedDate')


class CountryForm(forms.ModelForm):
    class Meta:
        model = CountryList
        fields = '__all__'
        exclude = ('IsActive',)


class UserJobPostForm(forms.ModelForm):
    class Meta:
        model = UserList
        fields = '__all__'
        exclude = ('password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'UserMiddleName', 'Application', 'usertype', 'groups', 'user_permissions', 'date_joined')