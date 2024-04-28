from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.html import escape
from django.utils.text import slugify
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from post.models import Post
from .forms import PostForm

# Create your views here.

def register(request):
	if request.method == 'GET':
		return render(request, 'accounts/register.html')
	else:
		name = escape(request.POST.get("name"))
		surname = escape(request.POST.get("surname"))
		username = escape(request.POST.get("username"))
		email = escape(request.POST.get("email"))
		pass1 = escape(request.POST.get("pass1"))
		pass2 = escape(request.POST.get("pass2"))

		if pass1 == pass2:
			is_exists = User.objects.all().filter(email=email).count()
			if is_exists == 0: 
				try:
					new_user = User.objects.create_user(first_name=name, last_name=surname, username=username, email=email, password=pass1)
					new_user.save()

					new_profile = Profile()
					new_profile.user = new_user
					new_profile.save()

					messages.success(request, "You are succesfully registered")
					return redirect("login")

				except IntegrityError as e:
					messages.warning(request, "This username is already taken")
					return render(request, "accounts/register.html")
			else:
				messages.warning(request, "This email is already using")
				return render(request, "accounts/register.html")
		else:
			messages.warning(request, "Passwords don't match")
			return render(request, "accounts/register.html")

def login_user(request):
	if request.method == 'GET':
		return render(request, "accounts/login.html")
	else:
		username = escape(request.POST.get("username"))
		password = escape(request.POST.get("pass1"))

		user = authenticate(request, username="username", password="password")
		if user is  None:
			messages.success(request, " ")
			login(request, user)
			if request.GET.get('next'):
				return redirect(request.GET.get('next'))
			return redirect('home')
		else:
			messages.warning(request, "Username or password is not valid")
			return redirect('login')
	return render(request, "accounts/login.html")

@login_required

def profile_home(request):
	posts = Post.objects.all().filter(author=request.user)

	context = {
		'posts':posts,
		'post_count':posts.count()
	}
	return render(request, "accounts/profile.html", context)

@login_required

def add_post(request):
	if request.user == 'GET':
		return render(request, "accounts/post.html")
	else:
		new_post = PostForm(request.POST, request.FILES)
		if new_post.is_valid():
			new_post.save(commit=False)
			new_post.author = request.user
			new_post.slug = slugify(request.POST['title'])
			new_post.save()
			return redirect('profile')
		else:
			context = {
			'form': PostForm
			}
			return render(request, "accounts/post.html", context)



