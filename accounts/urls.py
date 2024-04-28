from django.urls import path
from . import views

urlpatterns = [
	path('', views.profile_home, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('post/add', views.add_post, name='add_post'),
]
