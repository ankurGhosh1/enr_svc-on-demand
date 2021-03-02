from django.shortcuts import redirect, render
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.decorators import user_passes_test
from accounts.models import UserList, UserType
from django.db import connection

## Restricting user Mixin 

## Restricting Professionals

class ClientLoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.session['user']['is_authenticated']:
            return self.handle_no_permission()
        if self.request.session['user']['usertype_id'] == 2:
            # return render(request, 'clients/restricted.html')
            return redirect('/professional/explore')
        return super().dispatch(request, *args, **kwargs)


class ProfessinonalLoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.session['user']['is_authenticated']:
            return self.handle_no_permission()
        if self.request.session['user']['usertype_id'] == 1:
            return render(request, 'clients/restricted.html')
        return super().dispatch(request, *args, **kwargs)
