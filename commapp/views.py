import imp
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from .models import comm

from commapp.forms import commForm
# Create your views here.


def main(request):
    return render(request, 'main.html')

def board_post(request):
    if request.method == 'POST' or request.method=='FILES': #POST요청 폼의 버튼을 눌렀다
        form  = commForm(request.POST, request.FILES) #form 유효성 확인
        if form.is_valid():
            c = form.save(commit=False) #db에 당장 저장x
            c.save()
            return redirect('board_detail', pk = c.pk)
    else: #GET요청 웹 브라우저에서 페이지 접속
        form = commForm()
    return render(request, 'board_post.html', {'form':form})

def board(request):
    c = comm.objects.all()
    return render(request, 'board.html',{'comm':c})

def board_detail(request, pk):
    # all = comm.objects.all()
    c = get_object_or_404(comm, pk=pk)
    return render(request, 'board_detail.html',{'comm':c})

def board_update(request, pk):
    c = get_object_or_404(comm,pk=pk)
    if(request.method == "POST" or request.method == 'FILES'):
        form = commForm(request.POST, request.FILES, instance=c)
        if(form.is_valid()):
            c = form.save(commit=False)
            c.save()
        return redirect('board_detail', pk=c.pk)
    else:
        form = commForm(instance=c)
        return render(request, 'board_post.html', {'form':form})

def board_delete(request,pk):
    c = get_object_or_404(comm,pk=pk)
    c.delete()
    return redirect('board')


