from django.urls import path, include
from .views import (hello) 


urlpatterns = [
	path('hello/', hello, name='hello'),
	path('', BaseView, name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
]