

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path("logout",views.logout_request, name="logout"), 
    path('/resend',views.resend_otp),
    path('/password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('/password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_comeplete.html"),name="password_reset_complete")
]


