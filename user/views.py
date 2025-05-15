from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} - амжилттай бүртгэгдлээ!')
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_update(request):
    # 🛠️ staff гэж нэрлэсэн тул энд staff=request.user гэж бичнэ
    profile, created = Profile.objects.get_or_create(staff=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)
