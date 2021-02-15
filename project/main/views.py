from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pictures
# Create your views here.


@login_required
def home(request):
    context = {
        "pictures": Pictures.objects.all()
    }
    
    return render(request, "main/home.html", context)
