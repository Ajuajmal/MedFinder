



from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'login/index.html', context)
