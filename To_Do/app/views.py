from django.shortcuts import render,redirect
from .models import Task

def home(request):
    task=Task.objects.all()
    context={'tasks':task}
    if request.method=='POST':
        title=request.POST.get('title')

        Task.objects.create(title=title)
        return redirect('/')

    return render(request,"index.html",context)

def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    return render(request,'delete.html')
    



def update_task(request,pk):

    task=Task.objects.get(id=pk)

    if request.method=="POST":
        title=request.POST.get('title')
        task.title=title
        print(title)
        task.save()
        return redirect("/")
    return render(request,'update.html',{"task":task})
    

