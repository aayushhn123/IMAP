from django.shortcuts import render, HttpResponse, redirect
from .models import Blog, Comment

# Create your views here.

# def get_blogs(request):
    # return HttpResponse("<h1>Hello from Django !</h1>")


def get_blogs(request):
    
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'index.html', context=context)

def get_blog(request, blog_id: int):
    
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog_id=blog)
    context = {
        "blog": blog,
        "comments": comments
    }
    return render(request, 'post.html', context=context)


def create_comment(request, blog_id: int):
    
    if request.method == "POST":
        
        print(request.POST)
        comment = request.POST.get("comment", None)
        if comment is not None:
            
            blog = Blog.objects.get(id=blog_id)
            
            print(blog)
            
            c = Comment(
                content=comment,
                blog_id=blog
            )
            c.save()
            
            return redirect("get_blog", blog_id=blog_id)
            