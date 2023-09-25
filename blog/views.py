from django.shortcuts import render

from blog.models import Blog


def home(request):
    blog_data = Blog.objects.all()
    
    compailer = {
        'blog_data': blog_data,
    }

    return render(request, 'blog/home.html', compailer)