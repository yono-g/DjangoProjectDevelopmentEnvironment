from django.contrib.auth import views as auth_views
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='accounts.login'),
    path('', IndexView.as_view(), name='accounts.index'),
]
