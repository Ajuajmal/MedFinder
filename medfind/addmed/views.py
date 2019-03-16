# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import addmed
from django.shortcuts import render

# Create your views here.
def med_list(request):
    meds = addmed.objects.filter(updated_date__lte=timezone.now()).order_by('exp_date')
    return render(request,'addmed/addmed.html',{'meds': meds})
