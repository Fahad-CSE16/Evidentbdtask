from django.shortcuts import render
from .models import *
# Create your views here.
def khoj_the_search(request):
    if request.method=="POST":
        arr=request.POST['array']
        query=request.POST['query']
        arr = arr.split(",")
        arr=sorted(arr,reverse=True)
        if query in arr:
            result=True
        else:
            result=False
        Results.objects.create(user=request.user,result=result, search_value= query,input_values=arr )
        return render(request,'khoj/khoj.html',{'result':result})
    return render(request,'khoj/khoj.html')