from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages


# Create your views here.


def home(request):
    tasks = Task.objects.all()

    form = NoteForm()

    if request.method =='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(title__icontains=q) | Q(content__icontains=q) | Q(bucket__icontains=q))
        tasks = Task.objects.filter(multiple_q)
    else:
        tasks = Task.objects.all()
    
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tool/home.html', context) 
    

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = NoteForm(instance=task)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tool/update_task.html', context)

def delete_event(request,event_id):
    task =  Task.objects.get(pk=event_id)
    task.delete()
    return redirect('/')