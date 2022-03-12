from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout,
	organization_detail,
	) 


urlpatterns = [
	path('hello/', hello, name='hello'),
	path('', BaseView, name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('organization_detail/<str:slug>/', organization_detail, name='organization-detail'),
]