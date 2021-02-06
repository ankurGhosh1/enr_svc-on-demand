from django.contrib import admin
from .models import User, JobPost, ChatRecord, Category, SubCategory


# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ChatRecord)
admin.site.register(User)
admin.site.register(JobPost)
