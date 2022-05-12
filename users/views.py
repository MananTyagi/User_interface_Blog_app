from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm 
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form =UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

#for prevention of opening of profile page in case if logout without this it will black
#page if profile which is not fine 

@login_required
def profile(request):
    if request.method == 'POST':
        print(request.user.username)
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #for uploading files of image
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            print(request.user.username)
            print(request.user.profile.image)
            p_form.save()
            print(request.user.profile.image)
            
            messages.success(request,f'Your Account Updated !')
            return redirect('profile')


    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(request.FILES, instance=request.user.profile)
        
        
        
    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request, 'users/profile.html', context)
    
    
