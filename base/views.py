from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Post,Category,Likes
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PostForm
# Create your views here.

def home(request):
    if request.GET.get('q'):
        q = request.GET.get('q') 
        post_list = Post.objects.filter(Q(title__icontains=q)| Q(body__icontains=q)| Q(category__name__icontains=q)| Q(author__username__icontains = q))
    elif request.GET.get('category'):
        cat = request.GET.get('category')
        post_list = Post.objects.filter(Q(category__name__icontains=cat))
    else:
        post_list = Post.objects.all()

    p = Paginator(post_list,6)
    page = request.GET.get('page')
    posts = p.get_page(page)
    nums = 'a' * posts.paginator.num_pages

    num_of_post = len(post_list)

    likes = Likes.objects.filter(user=request.user.id)
    liked_posts = []

    for me in likes:
        liked_posts.append(me.post)
    
    category = Category.objects.all()
    context = {'posts':posts,'category':category,'nums':nums,'liked_posts':liked_posts,'num_of_post':num_of_post}
    return render(request,'base/home.html',context)
    
@login_required(login_url='login')
def post(request,post_id):
    category = Category.objects.all()
    post = Post.objects.get(pk=post_id)
    likes = Likes.objects.filter(user=request.user.id)
    liked_posts = []

    for me in likes:
        liked_posts.append(me.post)
    context = {'category':category,'post':post,'liked_posts':liked_posts}
    return render(request,'base/post.html',context)

@csrf_exempt
@login_required(login_url='login')
def create_post(request):
    categories = Category.objects.all()
    form = PostForm()
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST.get('title')
        category_name = request.POST.get('category').lower()
        category,created = Category.objects.get_or_create(name=category_name)
        body = request.POST.get('body')

        Post.objects.create(
            author = request.user,
            image=image,
            title=title,
            category=category,
            body = body
        )

        return redirect('home')
    context = {'form':form,'categories':categories}
    return render(request,'base/create_post.html',context)

@login_required(login_url='login')
def delete_post(request,post_id):
    post = Post.objects.get(pk=post_id)

    if request.user == post.author:
        post.delete()
        return redirect('home')
    else:
        return HttpResponse('You cant delete this post!')

@csrf_exempt
@login_required(login_url='login')
def update_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    categories = Category.objects.all()
    if request.user != post.author:
        return HttpResponse('You cant update this post!')

    form = PostForm(instance=post)

    if request.method == 'POST':
        category_name = request.POST.get('category')
        category,created = Category.objects.get_or_create(name=category_name)
        try:
            post.image = request.FILES['image']
        except:
            post.image = post.image
            
        post.title = request.POST.get('title')
        post.category = category
        post.body = request.POST.get('body')
        post.save()
        return redirect('home')

    context = {'form':form,'post':post,'categories':categories}
    return render(request,'base/update_post.html',context)

@csrf_exempt
def like_post(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        post = Post.objects.get(pk=int(id))

        filtered_post = Likes.objects.filter(post=id,user=request.user.id).first()

        liked = False
        
        if filtered_post == None:
            Likes.objects.create(post=id,user=request.user.id)
            post.like_count += 1
            post.save()
            liked = True
        else:
            Likes.objects.filter(post=id,user=request.user.id).first().delete()
            post.like_count -= 1
            post.save()
            liked = False

        like_count = post.like_count
        
        return JsonResponse({'like':like_count,'liked':liked})




