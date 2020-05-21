from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .models import universite


# Create your views here.
def index(request):
    return render(request,"giris_app/index.html")



def unv_yerles_giris(request):
    unv_list = universite.objects.all()
    return render(request,"giris_app/unv_yerles_giris.html", {'unv_list':unv_list}) 


def logout_view(request):
  
    logout(request)
    # Redirect to a success page.      
