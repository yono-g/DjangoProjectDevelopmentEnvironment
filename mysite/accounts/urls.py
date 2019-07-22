from django.contrib.auth import views as auth_views
from django.urls import path
from .views import IndexView
from .forms import EmailAuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            form_class=EmailAuthenticationForm
        ), name='accounts.login'),
    path('logout/', auth_views.LogoutView.as_view(), name='accounts.logout'),
    path('', IndexView.as_view(), name='accounts.index'),
]
