from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request): 

	feature1 = Feature()
	feature1.id = 0
	feature1.name = 'fast'
	feature1.details = 'mewo'
	feature1.is_true = True




	lists = [
		feature1,
		feature1,
		feature1,
		feature1
	]

	testfrombd = Feature.objects.all()
	

	context = {
		'name': 'nick',
		'age': '12',
		'nationality': 'Rus',
		'feature': feature1,
		'features': lists,
		'testfrombd': testfrombd
	}
	


	# return HttpResponse('<h1>Mewo</h1>')
	return render(request, 'index.html', context)


def counter(request):
	# words = request.GET['words']
	words = request.POST['words']

	posts = [1,2,3,4,5,6,7]


	amount_words = len(words.split())
	context = {
		"words": words,
		"posts": posts,
		'amount_words': amount_words
	}
	# print(words)

	return render(request, 'counter.html', context)


def register(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password2 == password:
			if User.objects.filter(email = email).exists():
				messages.info(request, 'Email is already created')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request, 'username is already used')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')

		else:
			messages.info(request, 'password not the same')
			return redirect('register')
	else:
		return render(request, 'register.html')

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else: 
			messages.info(request, 'credentials invalid')
			return redirect('login')
	else: 
		
		return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')
	


def post(request, pk):
	return render(request, 'post.html', {
		'pk': pk
	})