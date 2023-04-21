from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from base.models import Post,Category,Likes
from django.http import HttpResponseRedirect
# Create your views here.

@csrf_exempt
def user_register(request):
    page = 'register'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    form = UserForm()
    context = {'page':page,'form':form}
    return render(request,'account/login_register.html',context)

@csrf_exempt
def user_login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')

    context = {'page':page}
    return render(request,'account/login_register.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def user_profile(request,user_id):
    user = User.objects.get(pk=user_id)
    likes = Likes.objects.filter(user=request.user.id)
    liked_posts = []

    for me in likes:
        liked_posts.append(me.post)

    categories = Category.objects.all()
    posts = Post.objects.filter(author=user_id)
    num_of_post = len(posts)
    context = {'category':categories,'posts':posts,'user':user,'liked_posts':liked_posts,'num_of_post':num_of_post}
    return render(request,'base/profile.html',context)


@csrf_exempt
@login_required(login_url='login')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        try:
            user.avatar = request.FILES['profile-pic']
        except:
            user.avatar = user.avatar         
        user.website = request.POST.get('website')
        user.bio = request.POST.get('bio')
        user.save()

        return HttpResponseRedirect(f'profile/{request.user.id}')

    context = {'user':user}
    return render(request,'base/edit_profile.html',context)
