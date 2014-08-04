from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def snake(request):
    return render(request, 'snake.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()

    return render(request, 'registration/register.html',{
        'form': form
    })



def home(request):
    return render(request, 'base.html')

@login_required
def profile(request):
    return render(request, 'profile.html')



