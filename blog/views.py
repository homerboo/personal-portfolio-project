from django.shortcuts import render

def all_blogs(request):
    return render(request,'blogs/blogs.html')