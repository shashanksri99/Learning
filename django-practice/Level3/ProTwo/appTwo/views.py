from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import FormName
#from . import forms
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users' : user_list}
    return render(request,'appTwo/users.html', context=user_dict)

def form_page(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("Name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])

    return render(request, 'appTwo/formpage.html', {'form':form})
