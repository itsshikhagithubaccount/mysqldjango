from django.shortcuts import render, redirect,HttpResponse
from .form import *
from .models import *
# Create your views here.
def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = StudentsForm()
    context ={'form':form}
    return render(request,'index.html',context)
