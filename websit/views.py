from django.shortcuts import render
# Create your views here.


from django.http import HttpResponse,JsonResponse 

def index_view(request):
    return HttpResponse('<h1> home </h1>')

def about_view(request):
    return HttpResponse('<h1> about </h1>')

def about_contact(request):
    return HttpResponse('<h1> contact </h1>')
