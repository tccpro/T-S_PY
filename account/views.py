from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

from order.models import Order
from .models import User,Verification
from product.models import Product
from .send_sms import send_sms
def log_in(request):
    if request.method=='POST':
        password = request.POST.get('password')
        phone = request.POST.get('phone_number')
        customer = authenticate(password=password,phone_number=phone)
        if customer:
            login(request,customer)
            return redirect('home')
    return render(
        request=request,
        template_name='auth/login.html'
    )

def reset_password(request):
    if request.method=='POST':
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password1')
        user = request.user
        if password==user._password:
            print('yea')
        else:
            print(user.phone_number)
        customer = authenticate(password=password)
        if customer:
            login(request,customer)
            return redirect('home')
    return render(
        request=request,
        template_name='auth/reset.html'
    )


def verification(request):
    if request.method=='POST':
        code = request.POST.get('code',None)
        try:
            if code:
                verification = Verification.objects.get(code=code)
                user = verification.user
                user.is_verified = True
                user.save()
                login(request,user)
                return redirect('home')
            else:
                raise ValueError
        except:
            pass

    return render(
        request=request,
        template_name='auth/verification.html'
    )

def registration(request):
    user_message:str = ''
    password_message:str = ''
    if request.method=='POST':
        first_name = request.POST.get('first_name',None)
        last_name = request.POST.get('last_name',None)
        phone_number = request.POST.get('phone_number',None)
        password = request.POST.get('password',None)
        password1 = request.POST.get('password1',None)
        gender = request.POST.get('gender',None)
        user = User.objects.filter(phone_number=phone_number)
        if user:
            user_message = 'This phone number is busy'
        elif password==password1:
            user:User = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                password=password,
                phone_number=phone_number,
                gender=gender
            )
            user.set_password(password)
            user.save()
            verification = Verification.code_generate(user)
            send_sms(user.phone_number[1::],f'{verification.code}-Bu sizning tasdiqlash kodingiz. Uni hech kimga aytmang')
            return redirect('verification')
        else:
            password_message = 'Check your password'
    return render(
        request=request,
        template_name='auth/register.html',
        context={
            'user_message':user_message,
            'password_message':password_message,
        }
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def dashboard(request):
    orders = Order.objects.filter(customer=request.user)
    return render(
        request=request,
        template_name='account/dashboard.html',
        context={
            'orders':orders,
        }
    )