from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .views import IndexView
from .forms import EmailAuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            form_class=EmailAuthenticationForm
        ), name='accounts.login'),
    path('logout/', auth_views.LogoutView.as_view(), name='accounts.logout'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url=reverse_lazy('accounts.password_reset_done')
        ), name='accounts.password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ), name='accounts.password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('accounts.password_reset_complete')
        ), name='accounts.password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ), name='accounts.password_reset_complete'),

    path('', IndexView.as_view(), name='accounts.index'),
]
