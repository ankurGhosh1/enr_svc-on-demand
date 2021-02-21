from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField



class LanguageList(models.Model):
    LanguageName = models.CharField(max_length=100)

class AppliationList(models.Model):
    ApplicationName = models.CharField(max_length=100)
    Language = models.ForeignKey(LanguageList, on_delete=models.SET_NULL, null=True)


class UserType(models.Model):
    user_type = (
        ('Customer', 'Customer'),
        ('Professional', 'Professional')
    )
    UserType = models.CharField(max_length=15, choices=user_type, default="Customer")
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.UserType

class UserList(AbstractUser):
    UserMiddleName = models.CharField(max_length=100, null=True)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE)
    Application = models.ForeignKey(AppliationList,on_delete=models.CASCADE, null=True)
    ContactCell = models.CharField(max_length=100, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'usertype',
        'username',
        'first_name',
        'last_name',
    ]
    AbstractUser._meta.get_field('email')._unique = True

    def __str__(self):
        return self.email


class CountryList(models.Model):
    Country = models.CharField(max_length=100,blank=True,null=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.Country


class StateList(models.Model):
    State = models.CharField(max_length=100,blank=True,null=True)
    CountryId = models.ForeignKey(CountryList,on_delete=models.CASCADE, null=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.State

class CityList(models.Model):
    City = models.CharField(max_length=100)
    StateId = models.ForeignKey(StateList,on_delete=models.CASCADE, null=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    AddedBy = models.ForeignKey(UserList, on_delete=models.SET_NULL, null=True)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="City_Updated_By", on_delete=models.SET_NULL, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.City


class AddressList(models.Model):
    Street = models.CharField(max_length=500,blank=True,null=True)
    CityId = models.ForeignKey(CityList,on_delete=models.CASCADE, null=True)
    ZipCode = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.Street



class ResponseTypeList(models.Model):
    ResponseType = models.CharField(max_length=100)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Response_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

class TemplateTypeList(models.Model):
    SMSTemplateType = models.CharField(max_length=300)
    WhatsAppTemplateType = models.CharField(max_length=1000)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Template_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)



class CategoryList(models.Model):
    CategoryName = models.CharField(max_length=300)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Category_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.CategoryName



class CategoryInCity(models.Model):
    city = models.ForeignKey(CityList, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryList, null=True, on_delete=models.SET_NULL)




class SubCategoryList(models.Model):
    SubCategoryName = models.CharField(max_length=300)
    Category = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="SubCat_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.SubCategoryName


class SubscriptionList(models.Model):
    SubscriptionName = models.CharField(max_length=300)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Subscription_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)




class SubscriptionItemList(models.Model):
    SubscriptionItemName = models.CharField(max_length=300)
    DefaultValue = models.CharField(max_length=300)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Subscription_Item_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)





class ForceCloseCategoryList(models.Model):
    ForceCloseCategoryName = models.CharField(max_length=300)
    DefaultValue = models.CharField(max_length=300)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Force_Close_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)


class SubscriptionDetailList(models.Model):
    SubscriptionItemItem = models.CharField(max_length=300)
    ConfiguredValue = models.CharField(max_length=300)
    User = models.ForeignKey(UserList, related_name="Subscription_Details_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Subscription_Details_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)



class TopicList(models.Model):
    TopicName = models.CharField(max_length=300)
    content = HTMLField()
    TopicDate = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    City = models.ForeignKey(CityList, on_delete=models.CASCADE)
    User = models.ForeignKey(UserList, related_name="Topic_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Topic_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True,null=True)
    IsActive = models.BooleanField(default=True)
    IsClose = models.BooleanField(default=False)
    CloseBy = models.ForeignKey(UserList, related_name="Topic_Closed_By", on_delete=models.CASCADE, null=True)
    CloseDate = models.DateField(auto_now_add=True, null=True)
    ForceCloseReason = models.CharField(max_length=3999, null=True)
    ForceCloseCategory = models.ForeignKey(ForceCloseCategoryList, on_delete=models.SET_NULL, null=True)
    IsNotification = models.BooleanField(default=True)
    SMSText = models.CharField(max_length=150, null=True)
    WhatsAppText = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.TopicName

def get_upload_path(instance, filename):
    return '{0}/{1}'.format(instance.Topic.TopicName, filename)


class AssetsDetailList(models.Model):

    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    FileName = models.FileField(upload_to=get_upload_path)
    FileExtension = models.CharField(max_length=50, null=True, default=None)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Assets_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

class TopicDetailList(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    TopicDate = models.DateField(auto_now_add=True)
    User = models.ForeignKey(UserList, related_name="Topic_details_Subscriber", on_delete=models.CASCADE)
    Selected = models.BooleanField(default=False)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Topic_details_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)


class TopicSubCats(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    subcat = models.ForeignKey(SubCategoryList, on_delete=models.CASCADE)


class NotificationList(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    NotificationDate = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(CategoryList, on_delete=models.SET_NULL, null=True)
    SubCategory = models.ForeignKey(SubCategoryList, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(CityList, on_delete=models.SET_NULL, null=True)
    AssetsDetail = models.ForeignKey(AssetsDetailList, on_delete=models.SET_NULL, null=True)
    ToUser = models.ForeignKey(UserList, related_name="Notification_To_User", on_delete=models.CASCADE)
    User = models.ForeignKey(UserList, related_name="Notification_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Notification_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)


class ReviewList(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    ReviewDate = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(CategoryList, on_delete=models.SET_NULL, null=True)
    SubCategory = models.ForeignKey(SubCategoryList, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(CityList, on_delete=models.SET_NULL, null=True)
    ToUser = models.ForeignKey(UserList, related_name="Review_To_User", on_delete=models.CASCADE)
    FromUser = models.ForeignKey(UserList, related_name="Review_From_User", on_delete=models.CASCADE)
    ReviewNote = models.CharField(max_length=3999)
    AssetsDetail = models.ForeignKey(AssetsDetailList, on_delete=models.SET_NULL, null=True)
    User = models.ForeignKey(UserList, related_name="Review_Subscriber", on_delete=models.CASCADE, null=True)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Review_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True, null=True)
    IsActive = models.BooleanField(default=True)
    IsAdminApproved = models.BooleanField(default=True)


class ChatRecord(models.Model):
    client = models.ForeignKey(UserList, on_delete=models.CASCADE)
    professional = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name="professional")
    message = models.CharField(max_length=400)
    side = models.BooleanField(null=True, blank=True)   #True for consumer, False for professional
    room_name = models.CharField(max_length=300 )
    TimeStamp = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    topic = models.ForeignKey(TopicList, on_delete=models.CASCADE)


class OTP(models.Model):
    Otp = models.CharField(max_length=10)
    expire_minute = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    doc = models.DateTimeField(auto_now_add=True)
