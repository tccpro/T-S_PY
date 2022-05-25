from functools import wraps
from django.shortcuts import redirect

def is_verified(function):
        @wraps(function)
        def wrap(request,*args,**kwargs):
            if request.user.is_authenticated:
                if request.user.is_verified:
                    return function(request,*args,**kwargs)
                else:
                    return redirect('verification')
            else:
                return redirect('login')
        return wrap