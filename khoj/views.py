from django.shortcuts import render
from .models import *
import re
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def khoj_the_search(request):
    if request.method=="POST":
        arr=request.POST['array']
        query=request.POST['query']

        arr=re.split(',|;|, |,,|,',arr)
        
        print(arr)

        for i in arr:
            if i is None or i =='':
                arr.remove(i)
                print("call")
        try:
            arr = [int(i) for i in arr]
        except:
            messages.warning(request,'Please Provide Valid Coma separated integers')
            return render(request,'khoj/khoj.html')
        arr=sorted(arr,reverse=True)

        if int(query) in arr:
            result="True"
        else:
            result="False"
        print(arr)

        Results.objects.create(user=request.user,result=result, search_value= query,input_values=arr )
        return render(request,'khoj/khoj.html',{'result':result})
    return render(request,'khoj/khoj.html')