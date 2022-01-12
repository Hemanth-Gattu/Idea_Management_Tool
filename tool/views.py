from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q

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
        multiple_q = Q(Q(title__icontains=q) | Q(content__icontains=q))
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

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tool/delete.html', context)