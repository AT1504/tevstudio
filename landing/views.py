from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse
from .models import Developer

def index(request):#, developer_id):
    developer = Developer.objects.all() #get_object_or_404(Developer, pk=developer_id)
    return render(request, 'landing/index.html', {'developer': developer})
    #return HttpResponse("Hello, world. You're at the polls index.")