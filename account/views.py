from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from account.forms  import SignUpForm
from sendemailverification.send_email import send_custom_mail
from . models import Account,OtpEmail


#email parts
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives

import random

# Create your views here.




def logout_view(request):
    print(request.user,"*********************login user **********************")
    logout(request)
    return redirect("login")






def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            password = request.POST.get("password1")
            print(password,"from view function ======>>>>")
            user=form.save()
            user.set_password(password)
            user.is_active = False
            user.save()
            request.session['uid'] = user.pk
            token = default_token_generator.make_token(user)
            text = "please verify your student account !"
            send_custom_mail(request, user,text)
            return redirect('validate-email',token)
    else:
        form = SignUpForm()
    return render( request, "accounts/registration.html",{'form':form})



def validate_email(request,token):
    if request.method == "POST":
        uid = request.session['uid']
        otp_submit = str(request.POST.get('otp'))
        try:
            user = Account.objects.get(pk=uid)
            print(user)
            otp  = str(OtpEmail.objects.get(user=user))
            user_delete= OtpEmail.objects.get(user=user)
        except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
            user = None
            otp  = None
        if user is not None and default_token_generator.check_token(user,token) and otp is not None:
            request.session['pk_user']=user.pk
            if otp_submit ==str(otp):
                user.is_active = True
                user.save()
                user_delete.delete()
                return redirect('login')
            else:
                messages.error(request, "Opt does not match !")
                return redirect("validate-email",token)
    else:
        return render(request, "accounts/otp_verification.html")






def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        print(email)
        if Account.objects.filter(email__exact=email).exists():
            user =authenticate(username=email,password=password)
            print(user)
            if user:
                login(request, user)
                return redirect("bmi")
            else:
                messages.error(request, "incorrect password")
                return redirect('login')
        else:
            messages.error(request, "Please register first !")
            return redirect('login')
    return render(request, 'accounts/login.html')






def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Account.objects.filter(email__exact=email).exists():
            print("yes account exists")
            user = Account.objects.get(email=email)
            token = default_token_generator.make_token(user)
            request.session['user_id']=user.pk
            text = "please verify your student account !"
            send_custom_mail(request, user,text)
            messages.success(request, "check your email !")
            return redirect("forgotpassword-validate-email",token)

        else:
            print("account does not exists")
            messages.error(request, "please signup first")
    return render(request,"accounts/forgotpassword.html")



def forgotpassword_validate_view(request,token):
    if request.method == "POST":
        otp_submit = request.POST.get('otp').strip(" ")
        
        try:
            user = Account.objects.get(pk=request.session["user_id"])
            otp = OtpEmail.objects.filter(user=user).last()
            print(user,otp)
        except(TypeError,OverflowError,ValueError,Account.DoesNotExist,OtpEmail.DoesNotExist,KeyError):
            user = None
            otp = None

        if otp_submit == str(otp) and default_token_generator.check_token(user,token):
            return redirect("resetpassword")
        else:
            messages.error(request, "time over try again !")
            return redirect("forgetpassword")
    return render(request, "accounts/otp_verification.html")




def resetpassword_view(request):
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(password1,password2)
        if password1 == password2:
            user = Account.objects.get(id=request.session["user_id"])
            user.set_password(password1)
            user.save()
            otp = OtpEmail.objects.filter(user=user)
            otp.delete()
            messages.success(request, "password has been changed Succesfully !")
            return redirect("login")
        else:
            messages.error(request, "Both password are not same !")
            return redirect("resetpassword")
    else:
        return render(request, "accounts/resetpassword.html")





def profile_view(request):
    return render(request, "bmi-template/profile.html")