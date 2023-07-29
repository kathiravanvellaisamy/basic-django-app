from django.shortcuts import render,HttpResponse
from .models import BlogItem

# Create your views here.
def home(request):
    return render(request,'home.html')

def blogs(request):
    items = BlogItem.objects.all()
    return render(request, 'blog.html',{"blogs": items})
