from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
	path('', views.homepage, name='home'),
	path('colleges/', views.college_list, name='colleges'),
	path('college/<str:pk>/', views.college_branch, name='college_branch'),
	path('register/', views.register_view, name='register'),
	path('login/', views.login_view, name='login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
	path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
	path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]