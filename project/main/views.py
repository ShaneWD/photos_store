from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pictures
from django.core.paginator import Paginator
# Create your views here.


@login_required
def home(request):
    pictures = Pictures.objects.all()
    paginator = Paginator(pictures, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        # "pictures": pictures
    }
    
    return render(request, "main/home.html", context)

def detail(request, pk):
    picture = Pictures.objects.get(id=pk)
    context = {
        'picture': picture
    }
    return render(request, "main/detail.html", context)

