from django.urls import path
from websit.views import index_view,about_view,about_contact

urlpatterns = [
    path('home',index_view),
    path('about',about_view),
    path('contact',about_contact)
]
