from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout,
	OrganizationDetailView,
	) 


urlpatterns = [
	path('hello/', hello, name='hello'),
	path('', BaseView.as_view(), name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('organization_detail/<str:slug>/', OrganizationDetailView.as_view(), name='organization-detail'),
]