from django import forms
from models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app1.models import CustomUser
    

class PublicTrafficForm(forms.ModelForm):
    class Meta:
        model= TrafficFine
        fields=['full_name', 'reciept_no', 'offence', 'amount']

    def clean_full_name(self):
        full_name=self.cleaned_data.get("full_name")

        return full_name

    def clean_reciept_no(self):
        reciept_no=self.cleaned_data.get("reciept_no")

        return reciept_no

    def clean_offence(self):
        offence=self.cleaned_data.get("offence")

        return offence

    def clean_amt(self):
        amt=self.cleaned_data.get("amt")

        return amt


class PublicTrafficForm2(forms.ModelForm):
    class Meta:
        model= TrafficFine
        fields=['reciept_no']

    def clean_reciept_no(self):
        reciept_no=self.cleaned_data.get("reciept_no")

        return reciept_no



class FIRForm(forms.ModelForm):
    class Meta:
        model= FIR
        fields=['full_name', 'FIR_No', 'complaint']

    def clean_full_name(self):
        full_name=self.cleaned_data.get("full_name")

        return full_name

    def clean_FIR_no(self):
        FIR_No=self.cleaned_data.get("FIR_No")

        return FIR_No

    def clean_complaint(self):
        complaint=self.cleaned_data.get("complaint")

        return complaint



class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields=['full_name', 'email', 'rank', 'badge_no', 'message']

    def clean_full_name(self):
        full_name=self.cleaned_data.get("full_name")
        return full_name

    def clean_email(self):
        email= self.cleaned_data.get('email')
        return email

    def clean_rank(self):
        rank= self.cleaned_data.get('rank')
        return rank

    def clean_badge_no(self):
        badge_no= self.cleaned_data.get('badge_no')
        return badge_no

    def clean_message(self):
        message= self.cleaned_data.get('message')
        return message



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username"]

    # def __init__(self, *args, **kargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kargs)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username"]

    # def __init__(self, *args, **kargs):
    #     super(CustomUserChangeForm, self).__init__(*args, **kargs)



# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model= SignUp
#         fields=['full_name', 'email']

#     def clean_email(self):
#         email= self.cleaned_data.get('email')
#         # base, provider = email.split("@")
#         # dom, ext= provider.split(".")
#         # if not ext == ".com":
#         #     raise forms.ValidationError("Use valid col email address")
#         return email

#     def clean_full_name(self):
#         full_name=self.cleaned_data.get("full_name")
#         return full_name






