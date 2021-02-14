from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello</h1>")



def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, "users/profile.html", context)