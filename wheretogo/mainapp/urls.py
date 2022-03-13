from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout,
	OrganizationDetailView,
	NewsView,
	send_interest,
	get_recomendation,
	tour_view,
	FavouriteView,
	send_favourite,
	birth_day,
	family
	) 


urlpatterns = [
	path('hello/', hello, name='hello'),
	path('', BaseView.as_view(), name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('organization-detail/<str:slug>/', OrganizationDetailView.as_view(), name='organization_detail'),
	path('news/', NewsView.as_view(), name='news'),

	path('tour/', tour_view, name='tour'),
	path('favourite/', FavouriteView.as_view(), name='favourite'),
	path('birth_day/', birth_day, name='birth_day'),
	path('family/', family, name='family'),

	path('interest/', send_interest, name='interest'),
	path('recomentation/', get_recomendation, name='recomentation'),
	path('send-favourite/', send_favourite, name='send_favourite'),

	
]