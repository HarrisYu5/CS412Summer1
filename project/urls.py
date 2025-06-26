from django.urls import path
from .views import  *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('main/', MainPageView.as_view(), name='main'),
   path('registration/', RegistrationView.as_view(), name='registration'),
   path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
]
