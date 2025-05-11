from django.shortcuts import render, redirect
from .demo import *
import numpy
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

# df=pd.read_csv('tseamcet.csv')
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@login_required
def homepage(request):
	if request.method == 'POST':
		rank=int(request.POST.get('rank'))
		gender=str(request.POST.get('gender')) 
		caste=str(request.POST.get('caste'))
		branch=str(request.POST.get('branch'))

		# print(rank,gender,caste,branch)
		val=predict(rank,gender,caste,branch)
		
		vals=val.to_numpy().tolist()
		# print(vals)
		context ={'values':vals}
		return render(request,'results.html',context=context)

	return render(request,'homepagee.html')

@login_required
def college_list(request):
	res=list_of_colleges()
	context={'colleges':res}
	return render(request,'colleges_list.html',context)

@login_required
def college_branch(request,pk):
	branch=branch_list(pk)
	fee=fees(pk)
	context={'branches':branch,'Name':pk,'fee':fee}
	return render(request,'college.html',context)

@login_required
def college_branch_student(request,pk1,pk2):
	li=college_branch_data(pk1,pk2)
	li=li.to_numpy().tolist()
	total=len(li)
	context={'data':li,'Name':pk1,'Branch':pk2,'total':total}
	return render(request,'college_branch_student.html',context)

def register_view(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		phone_number = request.POST.get('phone_number')
		
		if password != confirm_password:
			messages.error(request, 'Passwords do not match!')
			return redirect('register')
			
		if User.objects.filter(email=email).exists():
			messages.error(request, 'Email already exists!')
			return redirect('register')
			
		user = User.objects.create_user(
			username=email,
			email=email,
			password=password
		)
		
		UserProfile.objects.create(
			user=user,
			phone_number=phone_number
		)
		
		login(request, user)
		messages.success(request, 'Registration successful!')
		return redirect('home')
		
	return render(request, 'registration/register.html')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password.')
	return render(request, 'login.html')

@login_required
def home(request):
	return render(request, 'home.html')

def terms_conditions(request):
	return render(request, 'terms_conditions.html')

def privacy_policy(request):
	return render(request, 'privacy_policy.html')
