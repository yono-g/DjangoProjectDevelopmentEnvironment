from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from sandbox.customauth.views import IndexView
from sandbox.customauth.forms import EmailAuthenticationForm

app_name = 'customauth'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='customauth/login.html',
            form_class=EmailAuthenticationForm
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('customauth/password_reset/', auth_views.PasswordResetView.as_view(
            template_name='customauth/password_reset.html',
            email_template_name='customauth/password_reset_email.html',
            subject_template_name='customauth/password_reset_subject.txt',
            success_url=reverse_lazy('customauth:password_reset_done')
        ), name='password_reset'),
    path('customauth/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='customauth/password_reset_done.html'
        ), name='password_reset_done'),
    path('customauth/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='customauth/password_reset_confirm.html',
            success_url=reverse_lazy('customauth:password_reset_complete')
        ), name='password_reset_confirm'),
    path('customauth/reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='customauth/password_reset_complete.html'
        ), name='password_reset_complete'),

    path('', IndexView.as_view(), name='index'),
]
