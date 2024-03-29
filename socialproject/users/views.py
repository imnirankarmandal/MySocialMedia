from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse("Invalid Credentials!")
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required()
def index(request):
    return render(request, 'users/index.html')