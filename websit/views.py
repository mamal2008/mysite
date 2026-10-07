from django.shortcuts import render

def index_view(request):
    return render(request,'websit/index.html')

def about_view(request):
    return render(request,'websit/about.html')

def about_contact(request):
    return render(request,'websit/contact.html')
