from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'CultureBox/home.html', context)

def about(request):
    return render(request, 'CultureBox/about.html', {'title':'About'})
