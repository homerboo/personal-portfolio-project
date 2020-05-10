from django.shortcuts import render
# from models import Blog
from .models import Blog 

def all_blogs(request):
    # Fetch from db
    blog = Blog.objects.all()
    context = {'blogs': blog}

    return render(request,'blogs/blogs.html', context)
