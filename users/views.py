from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

@login_required(login_url='account_login')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance = user)
    context = {
        'form':form
    }
    return render(request,'users/update.html',context)

@login_required(login_url='account_login')
def profile(request):
    user = request.user
    profile = get_object_or_404(User, user=user)
    
    context ={
        profile:profile
    }
    
    return render(request, 'users/profile.html', context)