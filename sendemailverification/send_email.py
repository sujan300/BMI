




from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from account.models import OtpEmail 


def send_custom_mail(request,user,text):
    otp = random.randint(100000, 500000)
    otp_create = OtpEmail.objects.create(otp=otp,user=user)
    otp_create.save()
    mail_subject = text
    message      = render_to_string(
        "email/email_verification.html",
        {
            "otp":otp,
            "user":user,
        }
    )
    to_email=user.email
    send_mail = EmailMultiAlternatives(mail_subject,message,to=[to_email])
    send_mail.attach_alternative(message,"text/html")
    send_mail.send()
    messages.success(request, "please check your email box")
    return True

    


