from django.urls import path 
from members import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('login/', LoginView.as_view(template_name = 'members/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'members/logout.html'), name='logout'),

]