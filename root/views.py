from django.shortcuts import render
from .models import Services

# Create your views here.

def home(request):
    return render(request,'root/index.html', context= {'name':'Roham Naeimi'})

def services(request):
    services = Services.objects.filter(statues = True)
    context = {
        'service':services
    }
    return render(request,'root/services.html', context = context)

def gallery_single(request):
    return render(request,'root/gallery-single.html')

def gallery(request):
    return render(request,'root/gallery.html')

def contact(request):
    return render(request,'root/contact.html')

def about(request):
    return render(request,'root/about.html')
