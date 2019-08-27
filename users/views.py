from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Update_profile, Update_img
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User

def register(request):

	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Account has been Created')
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = {
		'title' : 'Register',
		'form': form,
	}
	return render(request, 'users/register.html', context)


@login_required
def profile(request):
	posts = Post.objects.filter(author=request.user)[:5]
	context = {
		'title' : 'Profile',
		'posts' : posts,
	}

	return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
	if request.method == "POST":
		update_pro = Update_profile(request.POST, instance=request.user)
		img_update = Update_img(request.POST, request.FILES, instance=request.user.profile)
		if update_pro.is_valid() and img_update.is_valid():
			update_pro.save()
			img_update.save()
			messages.success(request, 'Your profile has been updated')
			return redirect('profile')
	else:
		update_pro = Update_profile(instance=request.user)
		img_update = Update_img(instance=request.user.profile)

	context = {
		'title' : 'Profile Update',
		'user_form': update_pro,
		'profile_form': img_update,
	}
	return render(request, 'users/edit_profile.html', context)
