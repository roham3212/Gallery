from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'root/index.html')

def services(request):
    return render(request,'root/services.html')

def gallery_single(request):
    return render(request,'root/gallery-single.html')

def gallery(request):
    return render(request,'root/gallery.html')

def contact(request):
    return render(request,'root/contact.html')

def about(request):
    return render(request,'root/about.html')