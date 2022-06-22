from ast import For
from pickle import TRUE
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog

# Create your views here.

data = {
    "blogs": [
        {
            "id":1,
            "title":"web geliştirme",
            "image":"pydjango.png",
            "is_active": False,
            "is_home": True,
            "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis illo voluptas autem."
        },
        {
            "id":2,
            "title":"mobil geliştirme",
            "image":"pydjango.png",
            "is_active": True,
            "is_home": True,
            "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."
        },
        {
            "id":3,
            "title":"yapay zeka geliştirme",
            "image":"pydjango.png",
            "is_active": True,
            "is_home": False,
            "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis illo voluptas autem."
        }
    ]
}


def index(request):
    context={
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context={
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):    
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {"blog": blog})


