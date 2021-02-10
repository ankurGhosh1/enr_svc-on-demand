from django.shortcuts import render
from django.db import connection
from django.views.generic import View




class HomeView(View):
    template_name = 'home.html'
    def get(self, request):
        users =[]
        if request.user.is_authenticated:
            if request.user.usertype=="Professional":
                with connection.cursor() as cursor:
                    cursor.execute(f'EXEC dbo.allUserTypeExceptMe @userId = {request.user.id}, @userType = "Customer"')
                    users = cursor.fetchall()
            else:
                with connection.cursor() as cursor:
                    cursor.execute(f'EXEC dbo.allUserTypeExceptMe @userId = {request.user.id}, @userType = "Professional"')
                    users = cursor.fetchall()
        context = {'users': users}
        # print(users)
        return render(request, self.template_name, context)
