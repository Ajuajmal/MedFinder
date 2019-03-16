



from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        if request.user.is_authenticated else []
    }

    return render(request, 'home/index.html', context)

def search(request):
    if request.method == 'GET': # this will be GET now
        book_name =  request.GET.get('search') # do some research what it does
        try:
            status = Add_prod.objects.filter(bookname__icontains=book_name) # filter returns a list so you might consider skip except part
        return render(request,"search.html",{"books":status})
    else:
        return render(request,"search.html",{})
