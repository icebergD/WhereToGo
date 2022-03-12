from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView, View, CreateView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.core import serializers

from .forms import UserLoginForm, UserRegistrationForm


def hello(request):
	return HttpResponse("Hello world")


def BaseView(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed,
		'username': request.user	
	}
	return render(request,'base.html',context)


def user_login(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed,
		'username':request.user

	}
	if request.method == 'POST':
		if not authed:
			form = UserLoginForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				user = authenticate(username=cd['username'], password=cd['password'])
				if user is not None:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect(reverse('base'))
				else:
					
					form = UserLoginForm()
					context['form'] = form
					return render(request, 'login.html', context)
			else:
				return HttpResponse('Not valid')
		return HttpResponse('Account logged alredy')
	else:
		form = UserLoginForm()
		context['form'] = form
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)


def user_register(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed,
		'username':request.user		
	}
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(username=cd['username'], first_name=cd['first_name'], email=cd['email'], password=cd['password'])
			user.save()
            
			return HttpResponseRedirect('/login/')
            # user = authenticate(username=cd['username'], password=cd['password'])
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         return HttpResponse('Register successfully')
            #     else:
            #         return HttpResponse('Disabled account')
            # else:
            #     return HttpResponse('Invalid register')
		else:
			context['form'] = form
	else:
		form = UserRegistrationForm()
		context['form'] = form
	return render(request, 'register.html', context)
   
def user_logout(request):
	authed = request.user.is_authenticated
	if authed:
		logout(request)
		authed = request.user.is_authenticated
	
	context = {
		'authed': authed,	
		'username':request.user	
	}
	return render(request,'logged_out.html',context)
