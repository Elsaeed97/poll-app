from django.shortcuts import render,redirect
from .models import Poll
from .forms import CreatePollForm
from django.http import HttpResponse
# Create your views here.

def index(request):
	polls = Poll.objects.all()
	context = {
		'polls':polls,
	}
	return render(request, 'index.html', context)

def create(request):
	if request.method == 'POST':
		form = CreatePollForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = CreatePollForm()
	context ={
		'form': form,
	}
	return render(request,'create.html',context)

def vote(request, id):
	poll = Poll.objects.get(id=id)
	if request.method == 'POST':
		selected = request.POST.get('poll')
		if selected == 'option1':
			poll.option_one_count += 1
		elif selected == 'option2':
			poll.option_two_count += 1
		elif selected == 'option3':
			poll.option_three_count += 1
		else:
			return HttpResponse("Unvalid Option")
		poll.save()
		return redirect('results',poll.id)

	context ={
		'poll': poll,
	}
	return render(request,'vote.html',context)

def results(request, id):
	poll = Poll.objects.get(id=id)

	context ={
		'poll':poll,
	}
	return render(request,'results.html',context)