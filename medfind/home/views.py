



from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        if request.user.is_authenticated else []
    }

    return render(request, 'home/index.html', context)
