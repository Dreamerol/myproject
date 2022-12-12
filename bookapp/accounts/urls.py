from django.urls import path

from bookapp.accounts.views import SignUpView, SignInView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('lol/', SignInView.as_view(), name='lol'),
# path('register/', SighUpView.as_view(), name='register'),
)