from django.contrib import admin
from .models import User, JobPost, ChatRecord


# Register your models here.
admin.site.register(ChatRecord)
admin.site.register(User)
admin.site.register(JobPost)
