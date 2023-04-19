from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('update_account/', views.update_account, name='update_account'),
    path('password/', views.change_password, name='change_password'),
    path('follow/<username>/', views.follow, name='follow'),
]