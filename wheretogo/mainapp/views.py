from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView, View, CreateView
from django.views import generic

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.core import serializers

from .forms import UserLoginForm, UserRegistrationForm
from .models import Organization, Like, OrganizationHashtag, UserHashtag

def hello(request):
	return HttpResponse("Hello world")


class BaseView(View):
	def get(self, request, *args, **kwargs):
		authed = request.user.is_authenticated
		context = {
			'authed': authed,
			'username': request.user	
		}
		if authed!=True:
			return HttpResponseRedirect(reverse('login'))

		# код для свайпа
		return render(request,'base.html',context)


class NewsView(View):
	def get(self, request, *args, **kwargs):
		new_list = Organization.objects.all().order_by('-creation_date')[:30]
		context = {
			'new_list': new_list,
		}
		return render(request,'news.html',context)


class OrganizationDetailView(View):
	def get(self, request, *args, **kwargs):
		organization_info = Organization.objects.get(slug=kwargs['slug'])

		context = {
			'organization_info': organization_info,
		}
		return render(request,'card.html',context)



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
