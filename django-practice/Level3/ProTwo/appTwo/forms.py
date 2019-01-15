from django import forms
#for using built in validators
from django.core import validators
#from appTwo.models import User

#creating your own validator using validators
# def check_for_z(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError("NAME SHOULD START WITH Z")

class FormName(forms.Form):
    name = forms.CharField() #(validators=[check_for_z])
    email = forms.EmailField()
    Verify_email=forms.EmailField(label='Enter your email again:')
    text =forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['Verify_email']

        if email!=vmail:
            raise forms.ValidationError("Emails donot match")
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    #creating your own deault validator
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_date['botcatcher']
    #     if if(botcatcher) > 0:
    #         raise forms.ValidationError("Gotta BOT!")
    #     return botcatcher
