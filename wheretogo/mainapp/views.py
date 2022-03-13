from django.shortcuts import render, redirect

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
from django.conf import settings

import random


from .forms import UserLoginForm, UserRegistrationForm
from .models import Organization, Like, OrganizationHashtag, UserHashtag

def hello(request):
	# return HttpResponse("Hello world")
	context = {
			'authed': 'authed',
			'username': "sfsd"
		}
	return render(request,'alajaxtest.html',context)


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



def send_favourite(request):
	if request.method == 'POST':
		if 'slug' in request.POST:
			organization = Organization.objects.filter(slug=request.POST['slug']).first()
			if organization:
				Like.objects.update_or_create(user=request.user, organization_id=organization)
			else:
				return JsonResponse({'response': "error"})

	return JsonResponse({'response': "got"})



def send_interest(request):
	if request.method == 'POST':
		if 'slug' in request.POST:
			organization = Organization.objects.filter(slug=request.POST['slug']).first()
			if organization:
				data = OrganizationHashtag.objects.filter(organization_id=organization)

				n_data = UserHashtag.objects.filter(user=request.user)
				UserHashtag.objects.filter(user=request.user).update(
					sport=n_data.first().sport + data.first().sport/10,
					art=n_data.first().art + data.first().art/10,
					health=n_data.first().health + data.first().health/10,
					alone=n_data.first().alone + data.first().alone/10,
					withcompany=n_data.first().withcompany + data.first().withcompany/10,
					adult=n_data.first().adult + data.first().adult/10,
					children=n_data.first().children + data.first().children/10,
					male=n_data.first().male + data.first().male/10,
					female=n_data.first().female + data.first().female/10,
					active=n_data.first().active + data.first().active/10,
					passiv=n_data.first().passiv + data.first().passiv/10,
					food=n_data.first().food + data.first().food/10

				)

			else:
				return JsonResponse({'response': "error"})

	return JsonResponse({'response': "got"})


def get_recomendation(request):
	if request.method == 'POST':
		

		n_data = UserHashtag.objects.filter(user=request.user)

		d = {
			'sport': n_data.first().sport, 
			'art': n_data.first().art,
			'health': n_data.first().health,
			'alone': n_data.first().alone,
			'withcompany': n_data.first().withcompany,
			'adult': n_data.first().adult,
			'children': n_data.first().children,
			'male': n_data.first().male,
			'female': n_data.first().female,
			'active': n_data.first().active,
			'passiv': n_data.first().passiv,
			'food': n_data.first().food
			}
		sorted_tuple = sorted(d.items(), key=lambda x: x[1])
		
		r1 = random.randint(0, 12)
		if r1 <= 4: # вероятность 5/13
			items = list(OrganizationHashtag.objects.order_by('-'+str(sorted_tuple[-1][0])).values())
			
		elif 4 < r1 <= 8: # вероятность 4/13
			items = list(OrganizationHashtag.objects.order_by('-'+str(sorted_tuple[-2][0])).values())

		elif 8 < r1 <= 11: # вероятность 3/13
			items = list(OrganizationHashtag.objects.order_by('-'+str(sorted_tuple[-3][0])).values())

		elif 11 < r1 <= 12: # вероятность 1/13
			items = list(OrganizationHashtag.objects.order_by('-'+str(sorted_tuple[-4][0])).values())
		item = random.choice(items)
		
		recomended_organization = list(Organization.objects.filter(id=item['organization_id_id']).values())
		recomended_organization[0]['image'] = str(settings.MEDIA_URL) + recomended_organization[0]['image']

		context = {
			'response': recomended_organization
		}
			
		
		return JsonResponse(context)


# def recomendations(request):
#     item = Organization.objects.all().order_by('-creation_date')[:30]
#     context = {
#         'item': item
#     }
#     return JsonResponse(context)

# class Recomendations(View):
# 	def get(self, request, *args, **kwargs):
# 		item = Organization.objects.all().order_by('-creation_date')[:30]
# 		context = {
# 			'item': item,
# 		}
# 		return render(request,'news.html',context)


class FavouriteView(View):
	def get(self, request, *args, **kwargs):
		like_list = Like.objects.filter(user=request.user)
		favourite_list = []

		for i in like_list:
			favourite_list += list(Organization.objects.filter(id=i.organization_id_id))

		context = {
			'favourite_list': favourite_list
		}
		return render(request,'favourites.html',context)


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


def tour_view(request):
	context = {
			'v': 's',
	}
	return render(request,'tour.html',context)


def birth_day(request):
	context = {
			'v': 's',
	}
	return render(request,'birth-day.html',context)

def family(request):
	context = {
			'v': 's',
	}
	return render(request,'family.html',context)
	




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
            
			uh = UserHashtag.objects.create(
				user=user
			)
			uh.save()

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
