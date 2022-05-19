from django.shortcuts import render,HttpResponse,redirect
from . models import  BMIMODEL,SuggestionModel
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.me 



# for email parts only 
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def sessions_store(request,height,weight,result,message,status):
    if height:
            request.session['height'] =height
            request.session['weight'] = weight
            request.session['result'] = result
            request.session['message'] = message.suggest_message
            request.session['status'] = message.status_suggestion
            return True
    else:
        return False

def get_session(request):
    print(request.session)
    if 'height' not in request.session:
        return False
    else:
        context = {
            'height':request.session['height'],
            'weight':request.session['weight'],
            'result':request.session['result'],
            'message':request.session['message'],
            'status':request.session['status'],
        }
        return context


def bmi_view(request):
    if request.method =="POST":
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        result = round((weight/(height*0.3048)**2),2)
        # suggestion_object = 
        color_status = None
        if result <= 18.5:
            status_suggestion = "Underweight"
            color_status = "red"
        elif result > 18.5 and result <= 23.0:
            status_suggestion = "Healthy"
            color_status='green'
        elif result >23.0 and result <=29.9:
            status_suggestion = "Overweight"
            color_status='rgb(165, 165, 36)'
        elif result > 30:
            status_suggestion = "Heavily overweight"
            color_status='blue'


        message=SuggestionModel.objects.get(status_suggestion__exact=status_suggestion)
        sessions_store(request=request,height=height,weight=weight,result=result,message=message,status=message.status_suggestion)


        return render(request, "bmi-template/bmi.html",{'result':result,'info':message,'color_status':color_status,'save_btn':get_session(request)})

    else:
        return render(request, "bmi-template/bmi.html")


@login_required(login_url='login')
def save_data_view(request):
    session_dict = get_session(request)
    height = session_dict.get('height')
    weight = session_dict.get('weight')
    result = session_dict.get('result')
    status = session_dict.get('status')
    suggest = session_dict.get('message')
    bmi = BMIMODEL.objects.create(height=height,weight=weight,result=result,status=status,suggest=suggest,user=request.user)
    # bmi.save()
    messages.success(request, "your data has been saved check out saved data section")
    return redirect("bmi")



@login_required(login_url="login")
def show_saved_data(request):
    data = BMIMODEL.objects.filter(user=request.user)
    return render(request, "bmi-template/savedbmi.html",{"data":data})




def delete_bmi_view(request,id):
    delete_bmi=BMIMODEL.objects.get(pk=id)
    delete_bmi.delete()
    messages.success(request,"deleted successfully !")
    return redirect("show-data")



@login_required(login_url="login")
def send_bmi_mail(request,id):
    bmi = BMIMODEL.objects.get(pk=id)
    mail_subject = "From Bmi Website Your Bmi"
    message      = render_to_string(
        "email/bmi_email.html",
        {
            "data":bmi,
        }
    )
    to_email=request.user.email
    send_mail = EmailMultiAlternatives(mail_subject,message,to=[to_email])
    send_mail.attach_alternative(message,"text/html")
    send_mail.send()
    messages.success(request, "please check your email box")
    return redirect("show-data")