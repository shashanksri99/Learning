from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import AccessRecord,Webpage,Topic
# Create your views here.
def help(req):
    my_dict = {"help_page":"This is the sample help page"}
    return render(req,'appTwo/help.html',context=my_dict)
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'appTwo/index.html',context=date_dict)
