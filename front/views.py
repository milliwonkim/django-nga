from django.shortcuts import render,redirect,get_object_or_404
from .models import Front
from django.utils import timezone 

#MAIN PAGE 연결
def front_main(request):
    front=Front.objects.all()
    return render(request, 'front_main.html',{'front':front})

#DETAIL PAGE 연결
def front_detail(request,pk):
    detail=Front.objects.get(pk=pk)
    return render(request,'front_detail.html',{'detail':detail})

#CRUD 함수
def front_write(request):
    return render(request,'front_write.html')

def front_edit(request,pk):
    front=Front.objects.get(pk=pk)
    return render(request,'edit.html',{'front':front})

def front_create(request):
    front=Front()
    front.start=request.POST['start']
    front.dest=request.POST['dest']
    front.title=request.POST['title']
    front.body=request.POST['body']
    front.save()
    return redirect('front_main')

def front_update(request,pk):
    front=Front.objects.get(pk=pk)
    front.start=request.POST['start']
    front.dest=request.POST['dest']
    front.title=request.POST['title']
    front.body=request.POST['body']
    front.save()
    return redirect('/front/main/'+str(front.id))

def front_delete(request,pk):
    front=Front.objects.get(pk=pk)
    front.delete()
    return redirect('front_main')

