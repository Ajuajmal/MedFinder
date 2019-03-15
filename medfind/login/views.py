



from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'login/index.html', context)
