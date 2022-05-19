from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup_view,name="signup"),
    path("validate-email/<token>/",views.validate_email,name="validate-email"),
    path('login/',views.login_view,name="login"),
    path('forgetpassword/',views.forgot_password_view,name="forgetpassword"),
    path("forgotpassword-validate-email/<token>/",views.forgotpassword_validate_view,name="forgotpassword-validate-email"),
    path("resetpassword/",views.resetpassword_view,name="resetpassword"),
    path('profile/',views.profile_view,name="profile"),
    path("logout/",views.logout_view,name="logout")

]