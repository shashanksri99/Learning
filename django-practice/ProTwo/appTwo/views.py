from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def help(req):
    my_dict = {"help_page":"This is the sample help page"}
    return render(req,'appTwo/help.html',context=my_dict)
def index(request):
    return HttpResponse("This is the index page")
