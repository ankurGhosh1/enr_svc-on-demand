from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class ClientLoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.usertype == 1:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)
