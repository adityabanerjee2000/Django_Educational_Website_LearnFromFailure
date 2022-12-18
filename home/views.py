from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.admin import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def courses(request):
    return render(request, 'courses.html')
    # return HttpResponse("this is courses page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

# Django follows MVT architecture.