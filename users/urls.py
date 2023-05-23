from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('votes/',views.votes,name='votes'),
    path('home/',views.home,name='home'),
    path('standings/',views.standings,name='standings'),
    path('votes/update/<int:id>', views.update, name='update'),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
]
