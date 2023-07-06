from django.shortcuts import render

from .models import Caption

# Create your views here.


def index(request):
    return render(request, 'myapp/base.html')


def home(request):
    captions = Caption.objects.all().order_by('-id')
    context = {'captions' : captions}
    return render(request, 'myapp/home.html', context)


def createPost(request):
    if request.POST.get('action') == 'newPost':
        title  = request.POST.get('title')
        description  = request.POST.get('description')
        image  = request.FILES.get('image')

        Caption.objects.create(
            title=title,
            description=description,
            image=image
        )

    return render(request, 'myapp/newPost.html')
