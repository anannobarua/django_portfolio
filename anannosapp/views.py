from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Portfolio
from .models import Contact

# Create your views here.
def index(request):
    about_data = About.objects.all()
    portfolio_data = Portfolio.objects.all()[:2]
    
    context = {
        'about_data': about_data,
        'portfolio_data': portfolio_data,
    }

    return render(request, 'index.html', context)

def single_port(request):
    portfolio_data = Portfolio.objects.all()
    
    simple = {
        'portfolio_data': portfolio_data,
    }
    return render(request,"main/single_port.html", simple)

def contact(request):
    return render(request,"main/contact.html")

def saveEn(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        description=request.POST.get('description')
        # Create variable
        # print(name,email,description)
        shower=Contact(name=name, email=email, description=description)
        shower.save()
        return HttpResponse("Submitted")
    return render(request, 'index.html')