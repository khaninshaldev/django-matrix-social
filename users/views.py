from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.
def loginAuth(request):
    form = AuthenticationForm()

    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('posts/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")    
            
            return redirect('home')

    context = {'form': form}
    return render(request, 'users/login.html', context)


def registerAuth(request):
    form = RegisterUserForm()

    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('posts/')
        else:
            messages.error(request, "Some error occured due to invalid information provided.")

    context = {'form': form}
    return render(request, 'users/register.html', context)

def logoutAuth(request):
    logout(request)

    return redirect('login')