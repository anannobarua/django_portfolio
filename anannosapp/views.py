from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
def index(request):
    # data={
    #     'student':'Welcome Bangladesh'
    # }
    data=About.objects.all()
    return render(request,'index.html', {'data':data})
#return render(request, 'appname/admin_data_list.html', {'admin_data_list': admin_data_list})