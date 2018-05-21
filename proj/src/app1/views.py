from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *

# from django.contrib.auth.models import User
from app1.models import CustomUser


def home(request):

    title="Welcome"
    messages = Message.objects.filter(read_status=False)
    
    if request.user.is_authenticated():
        title += ", %s" %(request.user.first_name)

    context = {
    "title": title,
    "messages": messages,
    }

    return render(request, 'home.html', context)



def traffic(request):

    title="Traffic Fine Registration"
    form=PublicTrafficForm(request.POST or None)
    messages = Message.objects.filter(read_status=False)

    if form.is_valid():
        form.save()
        form=PublicTrafficForm()

    context = {
    "form": form,
    "title": title,
    "messages": messages,
    }

    return render(request, 'traffic.html', context)


def traffic2(request):

    title="Traffic Fine Payment"
    form=PublicTrafficForm2(request.POST or None)
    messages = Message.objects.filter(read_status=False)

    ins=0
    
    if form.is_valid():

        rn=form.cleaned_data.get("reciept_no")

        if TrafficFine.objects.filter(reciept_no=rn):

            ins = TrafficFine.objects.get(reciept_no=rn)

            ins.status = 1
            ins.save()

            context = {
            "title": title,
            "full_name": ins.full_name,
            "reciept_no": ins.reciept_no,
            "offence": ins.offence,
            "amt":ins.amount,
            "status": ins.status,
            "messages": messages,
            }

            return render(request, 'traffic2.html', context)


        if ins==0:
            
            context = {
            "title": title,
            "form": form,
            "status": 0,
            "k": 0,
            "messages": messages,
            }
            return render(request, 'traffic2.html', context)

    context = {
    "title": title,
    "form": form,
    "status": 0,
    "k": 1,
    "messages": messages,
    }

    return render(request, 'traffic2.html', context)



def FIR(request):

    form=FIRForm(request.POST or None)
    title="First Information Report"
    messages = Message.objects.filter(read_status=False)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        form=FIRForm()

    context = {
    "form": form,
    "title": title,
    "messages": messages,
    }

    return render(request, 'FIR.html', context)



def wanted(request):

    title="MOST WANTED"
    messages = Message.objects.filter(read_status=False)

    context={
    "title": title,
    "messages": messages,
    }

    return render(request, 'wanted.html', context)



def passp(request):

    title="PASSPORT VERIFICATION"
    messages = Message.objects.filter(read_status=False)

    context = {
    "title": title,
    "messages": messages,
    }

    return render(request, 'passp.html', context)



def about(request):

    title="About"
    messages = Message.objects.filter(read_status=False)

    context = {
    "title": title,
    "messages": messages,
    }

    return render(request, 'about.html', context)



def contact(request):

    form = ContactForm(request.POST or None)
    title="Contact HQ"
    messages = Message.objects.filter(read_status=False)

    if form.is_valid():
        form.save()
        form=ContactForm()

        # for k in form.cleaned_data:
        #     print k + ': ' + form.cleaned_data[k]
        
        # form_message = form.cleaned_data.get("message")
        # form_full_name = form.cleaned_data.get("full_name")
        # form_rank = form.cleaned_data.get("rank")

        # subject = 'CONTACT FORM'
        # c_message = "%s: %s via %s"%(
        #     form_full_name,
        #     form_message, 
        #     form_precinct,
        #     form_rank)

        # from_email = settings.EMAIL_HOST_USER
        # to_email = [from_email]
       
        # send_mail(subject, 
        #     c_message, 
        #     from_email, 
        #     to_email, 
        #     fail_silently=True)

    context = {
    "form": form,
    "title": title,
    "messages": messages,
    }
    
    return render(request, "contact.html", context)


def messages(request):

    title="MESSAGE BOARD"
    messages = Message.objects.filter(read_status=False)
    messages1=Message.objects.all().order_by("-timestamp")

    for mess in messages1:
        if mess.read_status==False:
            mess.read_status=True
            mess.save()

    context = {
    "title": title,
    "messages1": messages1,
    "messages": messages,
    }

    return render(request, 'messages.html', context)



def profile(request):

    title = "PROFILE"
    messages = Message.objects.filter(read_status=False)

    profile = CustomUser.objects.get(username=request.user)

    context = {
    "title": title,
    "messages": messages,
    "profile": profile,
    }

    return render(request, 'profile.html', context)





