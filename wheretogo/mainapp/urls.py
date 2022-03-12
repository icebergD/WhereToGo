from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout,
	OrganizationDetailView,
	NewsView,
	) 


urlpatterns = [
	path('hello/', hello, name='hello'),
	path('', BaseView.as_view(), name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('organization-detail/<str:slug>/', OrganizationDetailView.as_view(), name='organization_detail'),
	path('news/', NewsView.as_view(), name='news'),
]