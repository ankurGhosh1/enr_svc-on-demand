from django.db import models
from django.contrib.auth.models import AbstractUser




class LanguageList(models.Model):
    LanguageName = models.CharField(max_length=100)

class ApplciationList(models.Model):
    ApplicationName = models.CharField(max_length=100)
    Language = models.ForeignKey(LanguageList, on_delete=models.SET_NULL, null=True)


class UserType(models.Model):
    UserType = models.CharField(max_length=100)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

class UserList(AbstractUser):
<<<<<<< HEAD
    UserType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    Application = models.ForeignKey(ApplciationList,on_delete=models.CASCADE)
=======
    UserMiddleName = models.CharField(max_length=100)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE)
    Application = models.ForeignKey(AppliationList,on_delete=models.CASCADE)
>>>>>>> 1063b8785d20a292866d9d196df172530257f046
    ContactCell = models.CharField(max_length=100)
    UserEmail = models.EmailField(max_length=100, unique=True)





class CityList(models.Model):
    City = models.CharField(max_length=100)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    AddedBy = models.ForeignKey(UserList, on_delete=models.SET_NULL, null=True)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="City_Updated_By", on_delete=models.SET_NULL, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)



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



class SubCategoryList(models.Model):
    SubCategoryName = models.CharField(max_length=300)
    Category = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="SubCat_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)


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
    TopicDate = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(SubCategoryList, on_delete=models.CASCADE)
    City = models.ForeignKey(CityList, on_delete=models.CASCADE)
    User = models.ForeignKey(UserList, related_name="Topic_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Topic_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    IsClose = models.BooleanField(default=True)
    CloseBy = models.ForeignKey(UserList, related_name="Topic_Closed_By", on_delete=models.CASCADE)
    CloseDate = models.DateField(auto_now_add=True)
    ForceCloseReason = models.CharField(max_length=3999)
    ForceCloseCategory = models.ForeignKey(ForceCloseCategoryList, on_delete=models.SET_NULL, null=True)
    IsNotification = models.BooleanField(default=True)
    SMSText = models.CharField(max_length=150)
    WhatsAppText = models.CharField(max_length=1000)


class AssetsDetailList(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    FileName = models.CharField(max_length=1000, null=True, default=None)
    FileExtension = models.CharField(max_length=50, null=True, default=None)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Assets_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

class TopicDetailList(models.Model):
    Topic = models.ForeignKey(TopicList, on_delete=models.SET_NULL, null=True)
    TopicDate = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(CategoryList, on_delete=models.SET_NULL, null=True)
    SubCategory = models.ForeignKey(SubCategoryList, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(CityList, on_delete=models.SET_NULL, null=True)
    AssetsDetail = models.ForeignKey(AssetsDetailList, on_delete=models.SET_NULL, null=True)
    User = models.ForeignKey(UserList, related_name="Topic_details_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Topic_details_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)



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
    User = models.ForeignKey(UserList, related_name="Review_Subscriber", on_delete=models.CASCADE)
    AddedBy = models.ForeignKey(UserList, on_delete=models.CASCADE)
    AddedDate = models.DateField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(UserList, related_name="Review_Updated_By", on_delete=models.CASCADE, null=True)
    UpdatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    IsAdminApproved = models.BooleanField(default=True)
